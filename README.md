# getYoutubeList
获取Youtube特定账号全部视频名称列表
昨天一个朋友说让看看youtube某栏目都有哪些视频，我想那就是要获取这个栏目发布的所有视频的标题，应该可以编程解决，问了下AI，给出了一个方案，主要就是使用YouTube Data API，需要在谷歌云里面配置下，获得一个API Key，然后本地python环境装个包，就可以编码调用相关API获取了。
步骤如下：

 1. 注册并获取API密钥：



访问 Google Cloud Console，创建一个新项目。在“API和服务”中启用YouTube Data API v3。创建API密钥。

创建API密钥的步骤如下：

访问Google Cloud Console：

打开浏览器，访问 Google Cloud Console。
创建新项目：

如果你还没有项目，点击页面顶部的“选择项目”下拉菜单，然后点击“新建项目”。
输入项目名称并选择一个结算账户（如果需要），然后点击“创建”。
启用YouTube Data API v3：

在左侧导航栏中，点击“API和服务” > “库”。
在搜索框中输入“YouTube Data API v3”，然后点击搜索结果中的“YouTube Data API v3”。
点击“启用”按钮来启用该API。
创建API密钥：

启用API后，返回到左侧导航栏，点击“API和服务” > “凭据”。
点击页面顶部的“创建凭据”按钮，然后选择“API密钥”。
系统会生成一个新的API密钥。你可以点击“限制密钥”来设置使用限制，以提高安全性。
保存API密钥：

复制生成的API密钥，并妥善保存。你将在脚本中使用这个密钥来访问YouTube Data API。

2.  安装必要的库：

使用Python编写脚本，并安装google-api-python-client库。

```bash
pip install google-api-python-client

