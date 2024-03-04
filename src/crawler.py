
class Crawler:
    '''
    A webcrawler that:
      1.) Navigates to a URL
      2.) Waits for elements at the URL to render
      3.) Finds certain elements 
      4.) Checks the file types of those elements
      5.) Collects the urls to those files in a list
    '''
    def __init__(self, url, file_type):
        self.url = url
        self.file_type = file_type
