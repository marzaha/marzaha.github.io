# Easy Gitee Pages介绍

之前采用Hexo搭建的Gitee Pages，markdown源文件备份比较麻烦，所以根据自己的思路搞了这个简易的Gitee Pages。

[访问地址]（http://jeytin.gitee.io/）

### 使用方法
目前根据我个人的需求，先添加了3个内容模块，分别是`日常笔记`、`图片示例`、`模拟数据`，见导航配置文件`nav.json`（该文件可根据个人需求自行修改）。

```json
[
    {
        "title": "日常笔记",
        "type": "blog"
    },
    {
        "title": "图片示例",
        "type": "photo"
    },
    {
        "title": "模拟数据",
        "type": "data"
    },
    {
        "title": "站内搜索",
        "type": "search"
    }
]
```

日常笔记文件仅支持markdown格式，放在`markdown`目录下，图片放在`photo`目录下，模拟数据以源文件形式放在`data`目录下。各类型文件添加之后，执行`generate.py`生成`config.json`，`index.html`打开时通过该文件统一管理各类型文件。


### markdown文件转html
参见 [markdeep](https://github.com/morgan3d/markdeep)

