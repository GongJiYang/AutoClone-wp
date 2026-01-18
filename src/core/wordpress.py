"""
WordPress REST API 客户端
"""
import requests
from typing import Optional
from .config import Config


class WordPressClient:
    """WordPress REST API客户端"""
    
    def __init__(self, site_url: str = None, username: str = None, app_password: str = None):
        self.site_url = (site_url or Config.WP_SITE_URL).rstrip('/')
        self.api_url = f"{self.site_url}/wp-json/wp/v2"
        self.auth = (username or Config.WP_USERNAME, app_password or Config.WP_APP_PASSWORD)
    
    def test_connection(self) -> bool:
        """测试WordPress连接"""
        try:
            response = requests.get(f"{self.api_url}/users/me", auth=self.auth)
            return response.status_code == 200
        except Exception as e:
            print(f"连接失败: {e}")
            return False
    
    def create_page(self, title: str, content: str, slug: Optional[str] = None, 
                    status: str = "draft") -> dict:
        """
        创建WordPress页面
        
        Args:
            title: 页面标题
            content: HTML内容
            slug: URL别名（可选）
            status: 状态 draft/publish/pending
        
        Returns:
            创建的页面信息
        """
        page_data = {
            'title': title,
            'content': content,
            'status': status,
        }
        
        if slug:
            page_data['slug'] = slug
        
        response = requests.post(
            f"{self.api_url}/pages",
            json=page_data,
            auth=self.auth
        )
        
        if response.status_code == 201:
            result = response.json()
            return {
                'success': True,
                'id': result['id'],
                'link': result['link'],
                'edit_link': f"{self.site_url}/wp-admin/post.php?post={result['id']}&action=edit"
            }
        else:
            return {
                'success': False,
                'error': response.text
            }
    
    def create_post(self, title: str, content: str, slug: Optional[str] = None,
                    status: str = "draft") -> dict:
        """创建WordPress文章"""
        post_data = {
            'title': title,
            'content': content,
            'status': status,
        }
        
        if slug:
            post_data['slug'] = slug
        
        response = requests.post(
            f"{self.api_url}/posts",
            json=post_data,
            auth=self.auth
        )
        
        if response.status_code == 201:
            result = response.json()
            return {
                'success': True,
                'id': result['id'],
                'link': result['link'],
                'edit_link': f"{self.site_url}/wp-admin/post.php?post={result['id']}&action=edit"
            }
        else:
            return {
                'success': False,
                'error': response.text
            }
