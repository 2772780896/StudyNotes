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
  #<div style={{ display: 'flex', alignItems: 'center' }}>
  #  <Menu onClick={onClick} selectedKeys={[current]} mode="horizontal" items={items} style={{ flex: 1, minWidth: 0 }}/>
  #</div>
   #通过用设定了flex的div包裹menu，实现menu稳定的flex实现
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