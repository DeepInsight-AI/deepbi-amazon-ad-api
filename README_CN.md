<div align="center">
  <img src="img/deepbi-logo.png" alt="DeepBI Logo" width="100" style="border-radius:20%"/>
  <h1 style="font-size:32px;margin:15px 0 5px">DeepBI - 亚马逊广告API</h1>
  <p style="font-size:18px;color:#555;margin:0 0 20px">AI驱动亚马逊广告优化专家</p>
  
  [English](README.md) | [中文](README_CN.md)
  
  <hr style="width:60%;margin:25px auto;border-top:1px solid #eee"/>
</div>

## 🚀 关于 DeepBI

> DeepBI为亚马逊卖家提供AI驱动的广告优化解决方案，通过智能策略匹配和数据分析，有效降低广告成本并提升ROI表现。

我们的核心优势:
- 🧠 **智能算法匹配** - 自动匹配最佳广告策略
- 💰 **CPC成本优化** - 降低点击成本，提高广告效率
- 📈 **ROI指标提升** - 科学分析，精准投放，提升投资回报
- 🔄 **全自动管理** - 简化广告投放流程，节省时间成本

**[立即访问官网 www.deepbi.com](https://www.deepbi.com)，开启智能广告管理之旅！**

---

## 🔧 API快速开始

这是一个Python 3封装的亚马逊广告API，提供简单易用的接口。

### 安装

```bash
pip install python-amazon-ad-api
```

### 基础使用

```python
from ad_api.api import sponsored_products

# 使用默认账户
result = sponsored_products.CampaignsV3().list_campaigns()

# 使用指定区域
from ad_api.base import Marketplaces
result = sponsored_products.CampaignsV3(marketplace=Marketplaces.NA).list_campaigns()
```

### 概述

您需要获取自己的Amazon凭证，包括Amazon开发者账户以及卖家或供应商访问权限。请查看[Amazon Ads API入门概述](https://advertising.amazon.com/API/docs/en-us/setting-up/overview)的检查表。


### 代码凭证
您可以通过将凭据作为字典传递给客户端来使用它们。

```javascript
from ad_api.api import sponsored_products


my_credentials = dict(
    refresh_token='your-refresh_token',
    client_id='your-client_id',
    client_secret='your-client_secret',
    profile_id='your-profile_id',
)

info = \
    {
        "stateFilter":
            {
                "include": [
                    "ENABLED"
                ]
            }
    }

result = sponsored_products.CampaignsV3(credentials=my_credentials).list_campaigns(
    body=info
)

```

### YAML凭证
使用credentials.yml文件存储您的凭证，更加方便地管理不同的账号或配置文件。Amazon要求每个市场一个配置文件，因此将所有配置保存在一个文件中并直接从代码中使用账户进行切换是很有用的。

创建credentials.yml文件：

```javascript
version: '1.0'

default:
  refresh_token: 'your-refresh-token'
  client_id: 'your-client-id'
  client_secret: 'your-client-secret'
  profile_id: 'your-profile-id'

germany:
  refresh_token: 'other-refresh-token'
  client_id: 'other-client-id'
  client_secret: 'other-client-secret'
  profile_id: 'other-profile-id'

```

Python代码：

```python
from ad_api.api import sponsored_products

# 留空将使用'default'账户
result=sponsored_products.CampaignsV3().list_campaigns()
# 使用德国账户数据
result=sponsored_products.CampaignsV3(account="germany").list_campaigns()
```

### credentials.yml的搜索路径

* macOS和其他Unix系统: `~/.config/python-ad-api`
* Windows: `%APPDATA%\python-ad-api`，其中<cite>APPDATA</cite>环境变量在未定义时默认为`%HOME%\AppData\Roaming`


[Confuse帮助文档](https://confuse.readthedocs.io/en/latest/usage.html#search-paths)


### 市场

市场主要用于定义Amazon需要使用的[API端点](https://advertising.amazon.com/API/docs/en-us/info/api-overview#api-endpoints)，这取决于地区。默认情况下，它将使用EU，因此如果您使用的是欧洲(EU)下的市场之一，包括英国、法国、意大利、西班牙、德国、荷兰、阿联酋、瑞典、波兰和土耳其，您可以跳过。如果您使用的是北美(NA)或远东(FE)，您需要从基础导入并传递市场，如下所示：

```python
from ad_api.api import sponsored_products
from ad_api.base import Marketplaces

# 您可以传递NA或US、CA、MX或BR代表北美，以及JP、AU或SG代表远东
result=sponsored_products.CampaignsV3(marketplace=Marketplaces.NA).list_campaigns()

```

### 异常处理

您可以在调用API时使用[try](https://docs.python.org/3.10/reference/compound_stmts.html#try)except语句捕获异常：

```python
from ad_api.api import sponsored_products
from ad_api.base import AdvertisingApiException

info = \
    {
        "stateFilter":
            {
                "include": [
                    "ENABLED"
                ]
            }
    }

try:

    result = sponsored_products.CampaignsV3().list_campaigns(
        body=info
    )

    logging.info(result)

except AdvertisingApiException as error:
    logging.info(error)
```

### 免责声明

我们与亚马逊没有关联，但他们使用了我们的API :)


> **归属说明**: 本项目基于[python-amazon-ad-api](https://github.com/denisneuf/python-amazon-ad-api)（MIT许可证）
> 原作者: Daniel Alvaro (denisneuf@hotmail.com) 和 Michael Primke


<div align="center">
  <p>© 2024 DeepBI - 专注AI驱动的亚马逊广告优化</p>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License"/>
</div> 