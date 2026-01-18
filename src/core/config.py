"""
配置管理模块
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Config:
    """统一配置管理"""
    
    # 项目根目录
    BASE_DIR = Path(__file__).parent.parent.parent
    
    # 目录配置
    DATA_DIR = BASE_DIR / "data"
    OUTPUT_DIR = BASE_DIR / "output"
    SCREENSHOT_DIR = OUTPUT_DIR / "screenshots"
    ANALYSIS_DIR = OUTPUT_DIR / "analysis"
    GENERATED_DIR = OUTPUT_DIR / "generated"
    ARCHIVE_DIR = BASE_DIR / "archive"  # 归档目录（移到主目录）
    
    # 视觉模型配置
    VISION_PROVIDER = os.getenv("VISION_PROVIDER", "zhipu")
    VISION_MODEL = os.getenv("VISION_MODEL", "glm-4.6v")
    ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # WordPress配置
    WP_SITE_URL = os.getenv("WP_SITE_URL")
    WP_USERNAME = os.getenv("WP_USERNAME")
    WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")
    
    # 截图配置
    VIEWPORT_WIDTH = 1440  # 增大视口宽度
    VIEWPORT_HEIGHT = 900
    OVERLAP = 150  # 增加重叠防止截断
    SCREENSHOT_QUALITY = 90
    PAGE_LOAD_WAIT = 5000  # 页面加载等待时间(ms)
    LAZY_LOAD_SCROLL_WAIT = 800  # 滚动后等待懒加载时间(ms)
    
    @classmethod
    def ensure_dirs(cls):
        """确保所有输出目录存在"""
        cls.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        cls.ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
        cls.GENERATED_DIR.mkdir(parents=True, exist_ok=True)
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def cleanup_output(cls, keep_archive: bool = True):
        """清空输出目录（可选保留归档）
        
        Args:
            keep_archive: 是否保留归档目录（默认True）
        """
        import shutil
        
        dirs_to_clean = [
            cls.SCREENSHOT_DIR,
            cls.ANALYSIS_DIR,
            cls.GENERATED_DIR,
        ]
        
        total_size = 0
        total_files = 0
        
        for dir_path in dirs_to_clean:
            if not dir_path.exists():
                continue
            
            # 统计文件大小
            for file in dir_path.rglob("*"):
                if file.is_file():
                    total_size += file.stat().st_size
                    total_files += 1
            
            # 删除目录
            shutil.rmtree(dir_path)
        
        # 重新创建目录
        cls.ensure_dirs()
        
        return total_files, total_size
    
    @classmethod
    def get_model_suffix(cls):
        """获取模型名称后缀（用于文件名，清理特殊字符）"""
        model = cls.VISION_MODEL
        # 替换不适合文件名的字符
        model = model.replace('.', '-').replace('/', '-').replace('\\', '-')
        model = model.replace(' ', '-').lower()
        return model
    
    @classmethod
    def validate(cls):
        """验证配置"""
        errors = []
        
        if cls.VISION_PROVIDER == "zhipu" and not cls.ZHIPU_API_KEY:
            errors.append("ZHIPU_API_KEY 未设置")
        elif cls.VISION_PROVIDER == "openai" and not cls.OPENAI_API_KEY:
            errors.append("OPENAI_API_KEY 未设置")
        
        if not cls.WP_SITE_URL:
            errors.append("WP_SITE_URL 未设置")
        if not cls.WP_USERNAME:
            errors.append("WP_USERNAME 未设置")
        if not cls.WP_APP_PASSWORD:
            errors.append("WP_APP_PASSWORD 未设置")
        
        return errors
