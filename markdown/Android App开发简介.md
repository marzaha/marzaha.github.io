﻿
# Android App开发简介

[TOC]

## 第一部分 开发流程

### 1. 明确需求

在App开发前，需要对App进行详细的分析。
- 产品定位（主题风格、受众群体、推广运营方式初步确定）
- 模块划分（模块化、插件化）
- 技术预研（所需的相关技术栈）

### 2. 工作量评估
根据产品的功能点初步预估App的界面数量（1.5个工作日）

### 3. 原型设计
App原型图类似于app的图纸，是app后期编程开发的核心。App原型图一般由产品经理根据前期沟通的开发需求，利用axure等原型工具绘制，主要包含app的功能点的实现、在页面上的排布、页面之间的交互跳转等。

[Axure示例](http://jeytin.gitee.io/axure)  

### 4. UI设计
产品定位及产品原型制作完善确定后，就可以交给设计师完成app的UI设计。App的UI设计图和开发出来的app非常相像，设计遵循简介美观、使用便捷的原则。一个好的UI设计可以直接提高app在用户心中的品牌印象；反之，则会降低用户的信任感、打开率等。

### 5. 编码
- 界面开发，依据UI设计图进行（客户端开发人员完成，开发时间可控）
- 接口调试（需要后台开发人员配合完成，开发时间不完全可控）

### 6. 测试
- 功能测试
- 性能测试

### 7. 上线
错误日志统计（友盟）

## 第二部分 常用控件和第三方库

### 1 四大组件
- Activity： 一个Activity通常就是一个单独的界面，可以理解为一个控制器，控制业务数据和组件的交互
- Service：用于在后台完成用户指定的操作，例如下载文件。
- BroadcastReceiver：对指定的外部事件进行过滤或做出相应（如来电或短信）。
- ContentProvider：用于程序之间数据共享，使一个应用程序的指定数据集能够提供给其他应用程序，如通讯录。

### 2 其他常用组件
- TextView
- ImageView
- EditText
- ListView
- GridView
- RelativeLayout
- LinearLayout
- SharedPreferences
- 其他

### 2 常用第三方库（基本）
- 网络调用：Okhttp
- 图片加载：Glide
- 数据解析：Gson
- 其他

### 3 简单案例
案例描述：实现用户登录功能。用户输入正确的用户名和密码登陆后，服务端返回用户详细信息，并缓存到客户端。

- 引用的第三方库（app/build.gradle）
```groovy
dependencies {
    implementation fileTree(dir: "libs", include: ["*.jar"])
    implementation 'androidx.appcompat:appcompat:1.2.0'
    implementation 'androidx.constraintlayout:constraintlayout:1.1.3'
    testImplementation 'junit:junit:4.12'
    androidTestImplementation 'androidx.test.ext:junit:1.1.1'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.2.0'
    //第三方库
    implementation 'com.squareup.okhttp3:okhttp:3.9.0'
    implementation 'com.google.code.gson:gson:2.2.4'
    implementation 'com.github.bumptech.glide:glide:3.6.1'
}
```

- 布局文件（activity_login.xml）
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:layout_margin="20dp">

    <TextView
        android:id="@+id/textview_login"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:text="用户登录" />

    <EditText
        android:id="@+id/textview_user_name"
        android:layout_width="200dp"
        android:layout_marginTop="10dp"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="请输入用户名" />

    <EditText
        android:id="@+id/textview_user_password"
        android:layout_width="200dp"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:layout_gravity="center"
        android:hint="请输入密码" />

    <Button
        android:id="@+id/button_user_login"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:layout_gravity="center"
        android:text="登录" />

</LinearLayout>
```

- 数据Model（UserInfo.java）
```java
package com.example.myapplication;

public class UserInfo {

    private int userId;
    private String userName;
    private String password;
    private String sex;
    private String birthday;
    private String imageUrl;

    public UserInfo() {
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getBirthday() {
        return birthday;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }
}

```

- 界面显示（LoginActivity.java）
```java
package com.example.myapplication;

import android.app.Activity;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.gson.Gson;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class LoginActivity extends Activity {

    private static final String BASE_URL = "http://192.168.1.1:80/";

    private EditText mEditTextName;
    private EditText mEditTextPwd;
    private Button mButtonLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        initView();
        registerClick();
    }

    private void initView() {
        mEditTextName = findViewById(R.id.textview_user_name);
        mEditTextPwd = findViewById(R.id.textview_user_password);
        mButtonLogin = findViewById(R.id.button_user_login);
    }

    private void registerClick() {
        mButtonLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                userLogin();
            }
        });
    }

    private void userLogin() {
        String name = mEditTextName.getText().toString();
        String password = mEditTextPwd.getText().toString();
        if (TextUtils.isEmpty(name)) {
            Toast.makeText(this, "请输入用户名", Toast.LENGTH_SHORT).show();
            return;
        }
        if (TextUtils.isEmpty(password)) {
            Toast.makeText(this, "请输入密码", Toast.LENGTH_SHORT).show();
            return;
        }
        loginPost(name, password);
    }

    private void loginPost(String name, String password) {
        String url = BASE_URL + "LoginServlet";
        OkHttpClient client = new OkHttpClient();
        FormBody.Builder builder = new FormBody.Builder();
        builder.add("name", name);
        builder.add("password", password);
        RequestBody requestBody = builder.build();
        Request request = new Request.Builder()
                .url(url)
                .post(requestBody)
                .build();
        Call call = client.newCall(request);
        call.enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                Toast.makeText(LoginActivity.this, "登陆失败", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                String result = response.body().string();
                UserInfo user = new Gson().fromJson(result, UserInfo.class);
                saveUserInfo(user);
            }
        });
    }

    private void saveUserInfo(UserInfo user) {
        SharedPreferences sp = getSharedPreferences("user", MODE_PRIVATE);
        SharedPreferences.Editor edit = sp.edit();
        edit.putInt("userId", user.getUserId());
        edit.putString("userName", user.getUserName());
        edit.putString("password", user.getPassword());
        edit.putString("sex", user.getSex());
        edit.putString("birthday", user.getBirthday());
        edit.putString("imageUrl", user.getImageUrl());
        edit.commit();
    }
}
```

## 第三部分 编码命名规范
> 参考（https://github.com/Blankj/AndroidStandardDevelop）

### 1 项目包名
包名全部小写，连续的单词只是简单地连接起来，不使用下划线，采用反域名命名规则，全部使用小写字母。一级包名是顶级域名，通常为 com、edu、gov、net、org 等，二级包名为公司名，三级包名根据应用进行命名。 包名是应用的唯一标识。示例：竞答系统App项目包名 `com.boya.exam`

### 2 类名

类名采用大驼峰命名法（`UpperCamelCase`）,通常是名词或名词短语，接口名称有时可能是形容词或形容词短语。
| 类                     | 描述                        | 例如                                       |
| :-------------------- | :------------------------ | :--------------------------------------- |
| `Activity` 类          | `Activity` 为后缀标识          | 欢迎页面类 `WelcomeActivity`                  |
| `Adapter` 类           | `Adapter` 为后缀标识           | 新闻详情适配器 `NewsDetailAdapter`              |
| 解析类                   | `Parser` 为后缀标识            | 首页解析类 `HomePosterParser`                 |
| 工具方法类                 | `Utils` 或 `Manager` 为后缀标识 | 线程池管理类：`ThreadPoolManager`<br>日志工具类：`LogUtils`（`Logger` 也可）<br>打印工具类：`PrinterUtils` |
| 数据库类                  | 以 `DBHelper` 后缀标识         | 新闻数据库：`NewsDBHelper`                     |
| `Service` 类           | 以 `Service` 为后缀标识         | 时间服务 `TimeService`                       |
| `BroadcastReceiver` 类 | 以 `Receiver` 为后缀标识        | 推送接收 `JPushReceiver`                     |
| `ContentProvider` 类   | 以 `Provider` 为后缀标识        | `ShareProvider`                          |
| 自定义的共享基础类             | 以 `Base` 开头               | `BaseActivity`, `BaseFragment`           |

### 3 方法名
方法名都以小驼峰命名法（ `lowerCamelCase`） 风格编写。方法名通常是动词或动词短语。
| 方法                          | 说明                                       |
| :-------------------------- | ---------------------------------------- |
| `initXX()`                  | 初始化相关方法，使用 init 为前缀标识，如初始化布局 `initView()` |
| `isXX()`, `checkXX()`       | 方法返回值为 boolean 型的请使用 is/check 为前缀标识      |
| `getXX()`                   | 返回某个值的方法，使用 get 为前缀标识                    |
| `setXX()`                   | 设置某个属性值                                  |
| `handleXX()`, `processXX()` | 对数据进行处理的方法                               |
| `displayXX()`, `showXX()`   | 弹出提示框和提示信息，使用 display/show 为前缀标识         |
| `updateXX()`                | 更新数据                                     |
| `saveXX()`, `insertXX()`    | 保存或插入数据                                  |
| `resetXX()`                 | 重置数据                                     |
| `clearXX()`                 | 清除数据                                     |
| `removeXX()`, `deleteXX()`  | 移除数据或者视图等，如 `removeView()`               |
| `drawXX()`                  | 绘制数据或效果相关的，使用 draw 前缀标识                  |

### 4 常量名
常量名命名模式为 `CONSTANT_CASE`，全部字母大写，用下划线分隔单词。
```java
private static final int SUCCESS_CODE = 200;
```

### 5 成员变量和类变量
非公有，非静态字段命名以 `m` 开头，静态字段命名以 `s` 开头，其他字段以小写字母开头。
```java
public class MyClass {
    public int publicField;
    private static MyClass sSingleton;
    int mPackagePrivate;
    private int mPrivate;
    protected int mProtected;
}
```

### 6 资源文件命名
- 布局文件
   
| 名称                          | 说明                          |
| --------------------------- | --------------------------- |
| `activity_main.xml`         | 主窗体 `类型_模块名`                |
| `activity_main_head.xml`    | 主窗体头部 `类型_模块名_逻辑名称`         |
| `fragment_music.xml`        | 音乐片段 `类型_模块名`               |
| `fragment_music_player.xml` | 音乐片段的播放器 `类型_模块名_逻辑名称`      |
| `dialog_loading.xml`        | 加载对话框 `类型_逻辑名称`             |
| `ppw_info.xml`              | 信息弹窗（PopupWindow） `类型_逻辑名称` |
| `item_main_song.xml`        | 主页歌曲列表项 `类型_模块名_逻辑名称`       |

- 颜色资源

```xml
  <resources>
      <!-- grayscale -->
      <color name="white"     >#FFFFFF</color>
      <color name="gray_light">#DBDBDB</color>
      <color name="gray"      >#939393</color>
      <color name="gray_dark" >#5F5F5F</color>
      <color name="black"     >#323232</color>
      <!-- basic colors -->
      <color name="green">#27D34D</color>
      <color name="blue">#2A91BD</color>
      <color name="orange">#FF9D2F</color>
      <color name="red">#FF432F</color>
  </resources>
```

- 字符串资源  

| 名称                  | 说明      |
| ------------------- | ------- |
| `main_menu_about`   | 主菜单按键文字 |
| `friend_title`      | 好友模块标题栏 |
| `friend_dialog_del` | 好友删除提示  |
| `login_check_email` | 登录验证    |
| `dialog_title`      | 弹出框标题   |
| `button_ok`         | 确认键     |
| `loading`           | 加载文字    |

- 其他（略）    



## 第四部分 跨平台解决方案
### 1 Cordova
 Cordova 是 Apache 旗下的跨平台解决方案，完全基于 html、css、js，写一次代码，Android和iOS两个平台都适用。开发方式和web前端开发方式相同，开发效率高，但响应速度较慢。
 
### 2 React-Native
 React-Native 是 Facebook 发布的一个前端框架，使用html、css、js编写代码，运行时在各平台渲染成原生组件展示。语法基于React，有一定学习门槛，相应速度基本与原生控件相同。

### 3 Weex
Weex是阿里巴巴发布的移动端跨平台解决方案，使用html、css、js编写代码，运行时在各平台渲染成原生组件展示。
语法基于Vue，有一定学习门槛，相应速度基本与原生控件相同。

### 4 Flutter
Flutter 是谷歌2018年发布的跨平台移动UI框架，使用Dart语言开发，内置渲染引擎，Android和iOS两端显示一致。（案例展示）





> PS：本文仅作内部交流培训使用，非专业文档。


