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
        #纯css中通过媒体查询限定特定条件下的style属性值来实现响应式
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

#滚动
    #创建一个滚动区域
        #<div ref={divRef} style={{ height: '400px', overflowY: 'auto',  position: 'relative' }}>
            #通过overflowY设置实现滚动条
            #通过height设置滚动区域的内容的高度
            #通过position设置滚动区域的定位
    #创建滚动区域中的内容，用于撑开滚动区域
        #<div style={{ height: '1000px' }}>
            #通过height设置内容的高度
            #内容高度大于滚动区域的高度时，滚动条才会出现
    #获取当前滚轮的位置
        #const divRef = useRef(null)
        #const [scrollTop, setScrollTop] = useState(0);  #动态更新滚动位置
        #useEffect(() => {  #使用useEffect来添加和移除滚动事件监听器
        #   const scrollElement = divRef.current;
        #   if (!scrollElement) {  #如果元素不存在，返回
        #       return;
        #   }
        #   const handleScroll = () => {  #定义滚动事件函数，setScrollTop更新滚动位置
        #       setScrollTop(scrollElement.scrollTop);  #通过scrollElement.scrollTop获取已滚动的像素数
        #   };
        #   scrollElement.addEventListener('scroll', handleScroll);  #添加滚动事件监听器，滚动时触发handleScroll函数
        #   return () => {
        #       scrollElement.removeEventListener('scroll', handleScroll);  #返回一个清理函数，移除事件监听器，防止内存泄漏
        #   };
        #}, []);
            #可滚动的最大像素数为1000px-400px=600px
            #可将scrollTop进行防抖处理，避免频繁更新
    #设置实际展示的内容
        #const itemHeight = 50 
            #设置每一个子项的高度
        #const itemCount = Math.ceil(400 / itemHeight)
            #设置子项数量
        #const startIndex = Math.floor(scrollTop / itemHeight)
            #计算已经滚动的子项数量
        #const sliceList = list.slice(startIndex, startIndex + itemCount)
            #通过slice方法获取当前展示的子项
    #创建实际展示的内容区域
        #<div style={{ position: 'absolute', top: {scrollTop}, width: '100%' }}>
        #    {sliceList.map(item => (
        #        <div key={item.id} style={{ height: itemHeight }}>
        #</div>
            #通过position与top设置实际内容的位置