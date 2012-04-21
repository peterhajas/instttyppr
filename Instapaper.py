import oauth2
import json
import urllib

class Instapaper:    
    root_url = "https://www.instapaper.com"
    
    def __init__(self,consumer_key,consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.consumer = oauth2.Consumer(consumer_key,consumer_secret)
        self.client = oauth2.Client(self.consumer)
        self.token = None
        self.token_secret = None
    
    def login(self,username,password):
        body = { }    
        body["x_auth_username"] = username
        body["x_auth_password"] = password
        body["x_auth_mode"] = "client_auth"
                
        body = urllib.urlencode(body)
        
        request_token_url = Instapaper.root_url + "/api/1/oauth/access_token"
        
        response,content = self.client.request(request_token_url,"POST",body=body,headers=self.headers())
        
        # If the response is invalid, return false. They presumably typed
        # something in wrong
        if content.find("Invalid") != -1:
            return False
        
        oauth_user_params = self.parse_qline(content)
        
        self.token = oauth_user_params['oauth_token']
        self.token_secret = oauth_user_params['oauth_token_secret']
        
        return True
    
    def list_bookmarks(self,folder_id=None):
        body = { }
        if folder_id is not None:
            body["folder_id"] = folder_id
        
        body = urllib.urlencode(body)
        
        list_bookmarks_url = Instapaper.root_url + "/api/1/bookmarks/list"
        
        response,content = self.client.request(list_bookmarks_url,"POST",body=body,headers=self.headers())
        print content
    
    def headers(self):
        http_headers = { }
        http_headers["oauth_consumer_key"] = self.consumer_key
        http_headers["oauth_consumer_secret"] = self.consumer_secret
        if self.token is not None:
            http_headers["oauth_token"] = self.token
        if self.token_secret is not None:
            http_headers["ouath_token_secret"] = self.token_secret
                
        return http_headers
    
    def parse_qline(self,string):
        parsed_value = { }
        
        string_components = string.split("&")
        
        for component in string_components:
            # Split by "="
            component_elements = component.split("=")
            parsed_value[component_elements[0]] = component_elements[1]
        
        return parsed_value
    