QRobot
======

微博机器人，树莓派专用~~

功能：
	每小时发一条密友微博，当然只供密友看的
	每天发几条普通微博
	当有新`@我的微博`的时候，给他一个评论

如果要运行，要在config文件夹下新建一个myConfig.py文件，该文件内容如下： 

	APP_KEY = '225488****'
	APP_SECRET = '3bd49f5d***********'  
	CALL_BACK = 'https://api.weibo.com/oauth2/default.html'
	CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
	USERID = '****登陆邮箱'
	PASSWD = '****密码'
