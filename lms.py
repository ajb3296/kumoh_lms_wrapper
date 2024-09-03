import requests

class Lms:
    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        }
        self.access_token = None
        self.refresh_token = None
        self.lms_user_id = None
        self.name = None
        self.email = None
    
    def login(self, username, password):
        """
        Login to LMS
        """
        res = requests.post("https://lms.kumoh.ac.kr:81/api/v1/signin", json={
            "userNumber": username,
            "password": password
        }, headers=self.header).json()
        self.access_token = res["accessToken"]
        self.refresh_token = res["refreshToken"]
        self.lms_user_id = res["lmsUserId"]
        self.name = res["name"]
        self.email = res["email"]
    
    def get_notification(self):
        """
        공지사항 가져오기
        """
        res = requests.get("https://lms.kumoh.ac.kr:81/api/v1/help/open-notification/all", headers=self.header | {
            "Authorization": "Bearer " + self.access_token
        })
        return res.json()

    def get_subject(self):
        """
        수강중인 과목 가져오기
        """
        res = requests.get("https://lms.kumoh.ac.kr:81/api/v1/subject/users/me/enrollment/all", headers=self.header | {
            "Authorization": "Bearer " + self.access_token
        })
        return res.json()
    
    def get_course_notice(self):
        """
        수강중인 과목에 대한 공지사항 가져오기
        """
        res = requests.get("https://lms.kumoh.ac.kr:81/api/v1/home/users/me/notice/all", headers=self.header | {
            "Authorization": "Bearer " + self.access_token
        })
        return res.json()

    def get_student_info(self, id):
        """
        학생 정보 가져오기
        """
        res = requests.get(f"https://lms.kumoh.ac.kr:81/api/v1/users?id={id}", headers=self.header | {
            "Authorization": "Bearer " + self.access_token
        })
        return res.json()