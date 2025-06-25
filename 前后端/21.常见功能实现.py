#前后端项目搭建
    #django环境搭建
    #app搭建，导入django
    #数据库配置
    #react文件夹npm初始化
    #react环境搭建

#前端分工
    #HTML代码
    #前端路由
    #数据提交

#后端分工
    #数据库交互
    #提供API，返回json数据
    #处理业务逻辑

#前端目录结构
    #src
        #assets  存放css文件
        #components  存放通用组件
            #common  存放通用小组件
            #feature  存放与具体业务相关，复用较少的组件
        #pages  存放页面级组件
        #hooks  存放自定义hook函数
        #utils  存放工具函数
        #apis  封装后端请求
        #router  前端路由配置
    #public  存放静态文件

#组件
    #导航栏
        #const items = [
        # {
        #   label: (<div></div>),
        #   key: 'icon',
        # },
        # {
        #   label: (<div></div>),
        #   key: 'main'
        # }
        #]
        #<Menu onClick={onClick} selectedKeys={[current]} mode="horizontal" items={items}/>
    #或者
        #<Menu onClick={onClick} selectedKeys={[current]} mode="horizontal">
        # <Menu.item key: 'icon'><Menu.item key: 'icon'>
        #     <div></div>
        # </Menu.item>
        # <Menu.item key: 'main'>
        #     <div></div>
        # </Menu.item>
        #</Menu>

    #布局
        #<Layout>
        #  <Header>
        #      <MenuApp />  直接调用封装好的menu即可
        #  </Header>



#布局
    #水平排列
        #Grid
            #<Row>
            #    <Col span={8}></Col>
            #    <Col span={16}></Col>
            #</Row>
        #Flex
            #<div style={{ display: 'flex' }}>
            #    <div style={{ flex: '0 0 30%', marginRight: 16 }}></div>
            #    <div style={{ flex: 1 }}></div>
            #</div>
            #<div style={{ display: 'flex' }}>
            #    <div style={{ width: '30%' }}></div>
            #    <div style={{ width: '70%', borderLeft: 'none' }}></div>
            #</div>
            #<Flex justify="space-between">
            #    <div style={{ width: '30%' }}></div>
            #    <div style={{ width: '70%' }}></div>
            #</Flex>
        #Flex设置其中元素的宽度
            #<Flex>
            #    <div style={{ flex: '1 1 100px' }}></div>
            #</Flex>
    #图片上显示文字
        #<div style={{position:'relative'}}>
        #     <img
        #         alt="example"
        #         src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png">
        #     </img>
        #     <div style={{
        #         position:'absolute',
        #         bottom:'0px',
        #         // position实现图片上显示文字
        #     }}
        #     >
        #         播放量 弹幕量
        #     </div>
        #</div>
    #响应式布局
        #纯css中通过媒体查询动态变更style属性值来实现响应式
        #Flex封装了媒体查询，自动进行响应式布局
        #Grid也可以自动进行响应式布局，也能通过断点手动设置响应式布局


#按钮函数传参
    #将函数的传参执行嵌入一个箭头函数中
        #<Button onclick={() => 函数名(参数)}></Button>

#Cookie设置与获取
    #document.cookie
        #设置
            #document.cookie = `my_token=${sessionToken}; expires=${expires}; path=/; SameSite=Lax; Secure`
        #获取
            #document.cookie // 返回值为 'my_token=F961286D-b5ac-6d67-4Bcf-A2b5AeB9C6Ed; uid=797; ...'
            #当需要获取特定名字的cookie时需要手动解析字符串
    #js-cookie
        #npm install js-cookie
        #import Cookies from 'js-cookie'
        #设置
            #Cookies.set('my_token', sessionToken, { expires: 7, path: '/', sameSite: 'Lax', secure: true })
        #获取
            #Cookies.get() // 返回值为 {uid: '157', my_token: 'fA7C08cA-AEd8-f2dE-d25A-604C01eCb4FF'}
            #当需要获取特定名字的cookie时，
                #Cookies.get('my_token')