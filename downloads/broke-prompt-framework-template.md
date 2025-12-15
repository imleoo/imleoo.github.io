# 钓鱼天气应用 - BROKE框架提示词

---

## ⚠️ 强制执行指令（CRITICAL）

### 必须遵守的约束
```
🔴 禁止行为（违反即失败）:
- 禁止输出 TODO、FIXME、待实现 等占位符
- 禁止输出 "此处省略"、"其他类似代码" 等省略说明
- 禁止使用 pass、NotImplementedError、throw "Not implemented"
- 禁止输出不完整的函数或类
- 禁止中途停止，必须完成所有模块
- 禁止跳过任何功能模块

🟢 必须执行（缺一不可）:
- 每个函数必须包含完整实现代码
- 每个API端点必须完整可运行
- 每个UI组件必须完整渲染
- 必须输出所有交付物清单中的文件
- 必须在最后输出功能完整性检查表
```

### 输出控制
```
如果上下文长度不足，按以下优先级输出：
1. 后端API完整代码 (最高优先级)
2. 前端核心页面代码
3. 数据库模型和迁移
4. 测试用例
5. 配置文件

⚠️ 无论如何，每个输出的文件必须是完整可运行的
```

---

## B - Background（背景）

### 项目背景
- **产品名称**: 钓鱼天气应用 (Fishing Weather App)
- **产品定位**: 面向钓鱼爱好者的综合性移动应用
- **核心价值**: 通过精准天气信息和钓鱼适宜度评估，帮助用户选择最佳钓鱼时机

### 目标用户
- 钓鱼爱好者（休闲和专业）
- 户外运动爱好者
- 对天气信息有特定需求的用户

### 技术栈
- **前端**: Flutter + Provider状态管理 + flutter_map地图组件
- **后端**: FastAPI + MySQL + JWT认证
- **API**: RESTful设计，天气数据来源wttr.in
- **存储**: shared_preferences本地存储 + 本地文件系统

### 技术约束
- 支持Android 5.0+和iOS 11.0+
- 适配不同屏幕尺寸和分辨率
- 支持横屏和竖屏模式
- 支持离线缓存机制

---

## R - Role（角色）

你是一位拥有10年移动应用开发经验的**全栈高级工程师**，具备以下专业能力：

### 技术专长
- **Flutter跨平台开发**: 精通Flutter框架，熟悉Provider状态管理、flutter_map地图集成
- **后端开发**: 精通FastAPI框架，熟悉RESTful API设计和JWT认证机制
- **数据库设计**: 精通MySQL数据库设计和优化
- **天气API集成**: 熟悉wttr.in等天气API的对接和数据处理

### 领域知识
- 了解钓鱼活动与天气条件的关联性
- 熟悉气象数据（气压、风速、温度、湿度等）对钓鱼的影响
- 了解移动应用的用户体验设计原则

### 工作风格
- 代码规范、注释清晰
- 遵循SOLID设计原则
- 注重代码可维护性和可扩展性
- **输出完整可运行代码，绝不使用占位符**

---

## O - Objectives（目标）

### 核心目标
一次性输出功能完整的钓鱼天气移动应用的**全部代码**，包括前端、后端、数据库、测试。

### 功能模块（必须全部实现）

#### 模块1: 天气与钓鱼适宜度 ✅必须
- [x] 自动获取当前位置（IP定位/GPS定位）
- [x] 城市搜索功能
- [x] 实时天气数据展示
- [x] 钓鱼适宜度评估算法（基于8项气象因素）
- [x] 未来3-7天天气预报
- [x] 详细钓鱼建议

#### 模块2: 用户认证 ✅必须
- [x] 邮箱注册/登录
- [x] JWT认证机制
- [x] 个人资料管理
- [x] 密码管理（修改/找回）

#### 模块3: 钓点分享 ✅必须
- [x] 创建钓点（位置、名称、描述、标签）
- [x] 查询钓点（按距离、名称）
- [x] 管理钓点（删除自己的钓点）
- [x] 地图展示钓点

#### 模块4: 鱼获分享 ✅必须
- [x] 上传鱼获（图片、描述、位置、标签）
- [x] 社区feed展示
- [x] 点赞/评论功能

#### 模块5: 地图功能 ✅必须
- [x] 地图显示钓点分布
- [x] 地图交互（缩放、平移、点击）
- [x] 地图上直接添加新钓点

#### 模块6: 设置与偏好 ✅必须
- [x] 多语言支持（中文/英文）
- [x] 离线缓存
- [x] 主题设置

---

## K - Key Results（关键结果）

### 钓鱼适宜度评估系统（必须完整实现算法）

```dart
// 必须输出完整的评分算法实现
class FishingScoreCalculator {
  static const Map<String, dynamic> scoringRules = {
    'pressure': {
      'optimal': [1005, 1015],  // 最佳+2分
      'good': [1015, 1025],     // +1分
      'poor': [0, 1005],        // -1分
    },
    'weather': {
      'sunny': 2,
      'cloudy': 1,
      'light_rain': 0,
      'fog': -1,
      'heavy_rain': -2,
    },
    'precipitation': {
      'low': [0, 30, 2],        // <30% +2分
      'medium': [30, 60, 0],    // 30-60% 0分
      'high': [60, 100, -1],    // >60% -1分
    },
    'cloud': {
      'optimal': [20, 60, 2],
      'acceptable': [0, 80, 0],
      'poor': [80, 100, -1],
    },
    'wind': {
      'optimal': [2, 10, 2],
      'acceptable': [0, 15, 0],
      'poor': [15, 100, -2],
    },
    'temperature': {
      'optimal': [15, 30, 2],
      'acceptable': [10, 35, 0],
      'extreme': [-50, 50, -2],
    },
    'humidity': {
      'optimal': [40, 80, 2],
      'acceptable': [30, 90, 0],
      'poor': [90, 100, -1],
    },
    'visibility': {
      'good': [5, 100, 2],
      'medium': [2, 5, 0],
      'poor': [0, 2, -2],
    },
  };

  // 完整实现计算方法...
}
```

### 适宜度等级
| 等级 | 分数范围 | 颜色标识 | 建议 |
|------|---------|---------|------|
| 极佳(Excellent) | ≥12分 | 🟢绿色 | 强烈推荐出钓 |
| 良好(Good) | 8-11分 | 🔵蓝色 | 适合出钓 |
| 一般(Moderate) | 4-7分 | 🟠橙色 | 可以考虑 |
| 较差(Poor) | <4分 | 🔴红色 | 不建议出钓 |

### 数据模型（必须完整定义）

```python
# 用户模型 - 必须包含所有字段
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    nickname = Column(String(100))
    avatar = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# 钓点模型 - 必须包含所有字段
class FishingSpot(Base):
    __tablename__ = "fishing_spots"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    tags = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

# 鱼获模型 - 必须包含所有字段
class Catch(Base):
    __tablename__ = "catches"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    image_url = Column(String(500), nullable=False)
    description = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    tags = Column(JSON)
    likes_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

# 互动模型 - 必须包含所有字段
class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    catch_id = Column(Integer, ForeignKey("catches.id"), nullable=False)
    type = Column(Enum("like", "comment"), nullable=False)
    content = Column(Text)  # 评论内容，点赞时为空
    created_at = Column(DateTime, default=datetime.utcnow)
```

### 性能指标
- 应用启动时间: <3秒
- 天气数据加载时间: <2秒
- 地图加载时间: <3秒
- 图片上传时间: <5秒

---

## E - Evolve（交付物清单）

### 必须输出的文件列表

#### 后端代码（FastAPI）
```
backend/
├── main.py                    # FastAPI入口，完整路由配置
├── config.py                  # 配置管理
├── database.py                # 数据库连接
├── models/
│   ├── __init__.py
│   ├── user.py               # 用户模型
│   ├── spot.py               # 钓点模型
│   └── catch.py              # 鱼获模型
├── schemas/
│   ├── __init__.py
│   ├── user.py               # 用户Pydantic模型
│   ├── spot.py               # 钓点Pydantic模型
│   ├── catch.py              # 鱼获Pydantic模型
│   └── weather.py            # 天气Pydantic模型
├── routers/
│   ├── __init__.py
│   ├── auth.py               # 认证路由（注册/登录/刷新）
│   ├── users.py              # 用户路由（资料/密码）
│   ├── weather.py            # 天气路由（获取/评分）
│   ├── spots.py              # 钓点路由（CRUD）
│   └── catches.py            # 鱼获路由（CRUD/互动）
├── services/
│   ├── __init__.py
│   ├── auth_service.py       # JWT认证服务
│   ├── weather_service.py    # 天气API服务
│   ├── fishing_score.py      # 钓鱼评分服务
│   └── file_service.py       # 文件上传服务
├── utils/
│   ├── __init__.py
│   ├── security.py           # 密码加密
│   └── dependencies.py       # 依赖注入
└── requirements.txt          # Python依赖
```

#### 前端代码（Flutter）
```
lib/
├── main.dart                  # 应用入口
├── config/
│   ├── app_config.dart       # 应用配置
│   ├── routes.dart           # 路由配置
│   └── theme.dart            # 主题配置
├── models/
│   ├── user.dart             # 用户模型
│   ├── weather.dart          # 天气模型
│   ├── fishing_score.dart    # 钓鱼评分模型
│   ├── spot.dart             # 钓点模型
│   └── catch.dart            # 鱼获模型
├── services/
│   ├── api_service.dart      # API基础服务
│   ├── auth_service.dart     # 认证服务
│   ├── weather_service.dart  # 天气服务
│   ├── spot_service.dart     # 钓点服务
│   ├── catch_service.dart    # 鱼获服务
│   └── storage_service.dart  # 本地存储服务
├── providers/
│   ├── auth_provider.dart    # 认证状态
│   ├── weather_provider.dart # 天气状态
│   ├── spot_provider.dart    # 钓点状态
│   ├── catch_provider.dart   # 鱼获状态
│   └── locale_provider.dart  # 语言状态
├── screens/
│   ├── splash_screen.dart    # 启动页
│   ├── home_screen.dart      # 首页（天气+评分）
│   ├── auth/
│   │   ├── login_screen.dart
│   │   └── register_screen.dart
│   ├── weather/
│   │   ├── weather_detail_screen.dart
│   │   └── forecast_screen.dart
│   ├── spots/
│   │   ├── spots_list_screen.dart
│   │   ├── spot_detail_screen.dart
│   │   └── add_spot_screen.dart
│   ├── catches/
│   │   ├── catches_feed_screen.dart
│   │   ├── catch_detail_screen.dart
│   │   └── add_catch_screen.dart
│   ├── map/
│   │   └── map_screen.dart
│   ├── profile/
│   │   ├── profile_screen.dart
│   │   └── edit_profile_screen.dart
│   └── settings/
│       └── settings_screen.dart
├── widgets/
│   ├── weather_card.dart     # 天气卡片
│   ├── fishing_score_card.dart # 钓鱼评分卡片
│   ├── spot_card.dart        # 钓点卡片
│   ├── catch_card.dart       # 鱼获卡片
│   └── common/               # 通用组件
│       ├── loading_widget.dart
│       ├── error_widget.dart
│       └── empty_widget.dart
├── utils/
│   ├── constants.dart        # 常量定义
│   ├── validators.dart       # 表单验证
│   └── helpers.dart          # 工具函数
└── l10n/
    ├── app_en.arb            # 英文翻译
    └── app_zh.arb            # 中文翻译
```

#### 测试代码
```
test/
├── unit/
│   ├── fishing_score_test.dart    # 钓鱼评分单元测试
│   ├── weather_service_test.dart  # 天气服务单元测试
│   └── auth_service_test.dart     # 认证服务单元测试
├── integration/
│   └── api_integration_test.dart  # API集成测试
└── backend/
    ├── test_auth.py              # 认证测试
    ├── test_weather.py           # 天气测试
    ├── test_spots.py             # 钓点测试
    └── test_catches.py           # 鱼获测试
```

#### 配置文件
```
├── pubspec.yaml              # Flutter依赖配置
├── docker-compose.yml        # Docker编排
├── Dockerfile               # 后端Docker配置
└── .env.example             # 环境变量示例
```

---

## 📋 功能完整性检查表（必须在最后输出）

完成所有开发后，**必须**输出以下检查表，确认每项功能已实现：

```
╔══════════════════════════════════════════════════════════════╗
║              功能完整性检查表 - 钓鱼天气应用                    ║
╠══════════════════════════════════════════════════════════════╣
║ 模块              │ 功能                    │ 状态          ║
╠══════════════════════════════════════════════════════════════╣
║ 天气模块          │ 位置获取（IP/GPS）        │ ✅/❌        ║
║                   │ 城市搜索                  │ ✅/❌        ║
║                   │ 实时天气显示              │ ✅/❌        ║
║                   │ 钓鱼评分算法              │ ✅/❌        ║
║                   │ 7天预报                   │ ✅/❌        ║
║                   │ 钓鱼建议                  │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 用户认证          │ 邮箱注册                  │ ✅/❌        ║
║                   │ 邮箱登录                  │ ✅/❌        ║
║                   │ JWT认证                   │ ✅/❌        ║
║                   │ 个人资料管理              │ ✅/❌        ║
║                   │ 密码修改                  │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 钓点模块          │ 创建钓点                  │ ✅/❌        ║
║                   │ 查询钓点                  │ ✅/❌        ║
║                   │ 删除钓点                  │ ✅/❌        ║
║                   │ 地图显示                  │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 鱼获模块          │ 上传鱼获                  │ ✅/❌        ║
║                   │ Feed展示                  │ ✅/❌        ║
║                   │ 点赞功能                  │ ✅/❌        ║
║                   │ 评论功能                  │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 地图模块          │ 地图显示                  │ ✅/❌        ║
║                   │ 地图交互                  │ ✅/❌        ║
║                   │ 地图添加钓点              │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 设置模块          │ 中英文切换                │ ✅/❌        ║
║                   │ 离线缓存                  │ ✅/❌        ║
║                   │ 主题设置                  │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 代码质量          │ 无TODO占位符              │ ✅/❌        ║
║                   │ 无省略代码                │ ✅/❌        ║
║                   │ 所有函数完整实现          │ ✅/❌        ║
║                   │ 测试用例输出              │ ✅/❌        ║
╚══════════════════════════════════════════════════════════════╝

总计: XX/30 项完成
完成率: XX%
```

---

## 🧪 测试要求

### 测试用例文档
必须输出完整的测试用例，覆盖以下场景：

```
必须覆盖的测试场景:
├── 钓鱼适宜度计算
│   ├── 最佳天气条件 → 预期分数 ≥12
│   ├── 最差天气条件 → 预期分数 <4
│   ├── 边界值测试（各因素临界点）
│   └── 空数据/异常数据处理
├── 用户认证
│   ├── 正常注册流程
│   ├── 重复邮箱注册
│   ├── 正常登录流程
│   ├── 错误密码登录
│   ├── Token验证和刷新
│   └── Token过期处理
├── 钓点操作
│   ├── 创建钓点（正常/缺失字段）
│   ├── 查询钓点（按距离/按名称）
│   ├── 删除钓点（自己的/他人的）
│   └── 权限验证
├── 鱼获互动
│   ├── 上传鱼获（正常/超大图片）
│   ├── 点赞/取消点赞
│   ├── 评论/删除评论
│   └── Feed分页加载
└── 边界情况
    ├── 空数据处理
    ├── 无效输入处理
    ├── 网络异常处理
    └── 并发请求处理
```

### 测试报告格式
完成所有开发后，必须输出以下格式的测试报告：

```
╔═══════════════════════════════════════════════════════════════╗
║                        测试报告                                ║
╠═══════════════════════════════════════════════════════════════╣
║ 📅 测试时间: [YYYY-MM-DD HH:MM:SS]                            ║
║ 📦 项目名称: 钓鱼天气应用                                      ║
║ 🔧 测试环境: Flutter 3.x / FastAPI 0.100+ / MySQL 8.0        ║
╠═══════════════════════════════════════════════════════════════╣
║                        📊 测试概览                             ║
╠═══════════════════════════════════════════════════════════════╣
║ 指标              │ 数值                                       ║
║ 总用例数          │ XX                                        ║
║ 通过              │ XX ✅                                      ║
║ 失败              │ XX ❌                                      ║
║ 跳过              │ XX ⏭️                                      ║
║ 通过率            │ XX%                                        ║
║ 覆盖率            │ XX%                                        ║
╠═══════════════════════════════════════════════════════════════╣
║                      📋 模块测试详情                            ║
╠═══════════════════════════════════════════════════════════════╣
║ 1. 天气模块 [X/Y 通过]                                        ║
║    ✅ test_weather_api_call                                   ║
║    ✅ test_fishing_score_optimal                              ║
║    ✅ test_fishing_score_poor                                 ║
║    ✅ test_fishing_score_boundary                             ║
║                                                               ║
║ 2. 用户认证模块 [X/Y 通过]                                    ║
║    ✅ test_user_register_success                              ║
║    ✅ test_user_register_duplicate                            ║
║    ✅ test_user_login_success                                 ║
║    ✅ test_user_login_wrong_password                          ║
║    ✅ test_jwt_validation                                     ║
║    ✅ test_jwt_refresh                                        ║
║                                                               ║
║ 3. 钓点模块 [X/Y 通过]                                        ║
║    ✅ test_create_spot_success                                ║
║    ✅ test_query_spots_by_distance                            ║
║    ✅ test_delete_own_spot                                    ║
║    ❌ test_delete_other_spot (应返回403)                       ║
║                                                               ║
║ 4. 鱼获模块 [X/Y 通过]                                        ║
║    ✅ test_upload_catch                                       ║
║    ✅ test_like_catch                                         ║
║    ✅ test_unlike_catch                                       ║
║    ✅ test_comment_catch                                      ║
║                                                               ║
║ 5. 边界情况测试 [X/Y 通过]                                    ║
║    ✅ test_empty_data_handling                                ║
║    ✅ test_invalid_input_validation                           ║
║    ✅ test_network_error_recovery                             ║
╠═══════════════════════════════════════════════════════════════╣
║ ❌ 失败用例详情                                                ║
║ [列出失败的测试用例及错误信息]                                  ║
╠═══════════════════════════════════════════════════════════════╣
║ 📝 测试结论                                                    ║
║ [总体评估和建议]                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📝 使用说明

将此提示词发送给AI，将获得：

1. ✅ 完整的后端API代码（FastAPI，所有端点可运行）
2. ✅ 完整的前端代码（Flutter，所有页面可渲染）
3. ✅ 完整的数据库模型和迁移脚本
4. ✅ 完整的测试用例（单元测试+集成测试）
5. ✅ 功能完整性检查表（确认所有功能已实现）
6. ✅ 测试执行报告

### 验收标准
- [ ] 所有30项功能全部实现（检查表全部✅）
- [ ] 代码无TODO、无占位符、无省略
- [ ] 测试用例覆盖率 ≥ 80%
- [ ] 测试报告已输出
- [ ] 所有文件可直接运行

---

## ⚡ 快速开始提示

如需快速获取完整代码，可直接发送：

```
请根据上述BROKE框架提示词，一次性输出钓鱼天气应用的完整代码。
要求：
1. 输出所有后端API代码
2. 输出所有前端Flutter代码
3. 输出所有测试代码
4. 最后输出功能完整性检查表和测试报告
5. 禁止使用TODO、禁止省略代码、所有函数必须完整实现
```
