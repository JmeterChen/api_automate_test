# coding=utf-8
import requests


# 推送钉钉消息调用方法（消息内容@手机号，手机号）
def send_ding(robot_url, mobile, content=None):
    """
    :param robot_url:         各个项目钉钉群内新增的机器人 url，必填参数
    :param mobile:            推送消息指定@对象，传入参数为 list对象，必填参数
    :param content:           推送消息内容，默认为None， 非必填
    :return:
    """
    if robot_url and content and mobile:
        robot_url = robot_url
        robot_body = {
            "msgtype": "text",
            "text": {
                "content": content
            },
            "at": {
                "atMobiles": mobile,
                "isAtAll": False
            }
        }
        r = requests.post(robot_url, json=robot_body)
        if r.status_code == 200:
            return True
        else:
            return False


# 钉钉推送测试报告调用方法（标题，内容，文件链接）
def send_link(robot_url, result_path, tittle='测试报告', text='点击查看本次所有项目的测试用例执行详情'):
    """
    :param robot_url:          各个项目钉钉群内新增的机器人 url，必填参数
    :param result_path:        项目测试结果报告路径，必填参数
    :param tittle:             推送测试报告链接 title，默认为None
    :param text:               测试报告简介内容，默认为None
    :return:
    """
    # robot_url = "https://oapi.dingtalk.com/robot/send?access_token
    # =bd92a2ab1bd3243084849ffb96506e1620359581b97b49bafe870ba640b014c1"
    # url = robot_url,
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=c41f688c4e87a482459697c9675d7a12dc6ebfbec9c242ccf' \
    #             '2b498bcece2644a'
    robot_body = {
        "msgtype": "link",
        "link": {
            "text": text,
            "title": tittle,
            "picUrl": "http://static.esf.fangdd.com/esf/factoringwebsiteesffdd/icon_fdd-1_tvW.svg",
            "messageUrl": result_path}
    }
    r = requests.post(robot_url, json=robot_body)
    if r.status_code == 200:
        return True
    else:
        return False


if __name__ == '__main__':
    
    robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=c41f688c4e87a482459697c9675d7a12dc6ebfbec9c242ccf' \
                '2b498bcece2644a'
    result_path = 'http://localhost:63342/api_automate_test/output/report/report_2019_09_11-17_14_43/2019_09_11-17_' \
                  '14_43_result.html'
    # print(send_ding(robot_url, ["18682236985", "17770035302", "15890608240"], "糟糕出错啦！"))
    print(send_link(robot_url, result_path))