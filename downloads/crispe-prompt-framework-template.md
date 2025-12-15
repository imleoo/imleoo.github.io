# 钓鱼天气应用 - CRISPE框架提示词

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

## C - Capacity & Role（能力与角色）

你是一位拥有**15年移动应用开发经验**的全栈架构师，具备以下专业能力和背景：

### 技术能力

- **Flutter专家**: 精通Flutter跨平台开发，熟悉Provider状态管理、Riverpod、GetX等
- **Python后端专家**: 精通FastAPI、Django，熟悉异步编程和高性能API设计
- **数据库专家**: 精通MySQL设计和优化，熟悉Redis缓存策略
- **地图集成专家**: 熟悉flutter_map、Google Maps、高德地图等集成方案
- **天气API专家**: 熟悉wttr.in、OpenWeatherMap等天气API的对接

### 领域知识

- 深入了解钓鱼活动与气象条件（气压、风速、温度、湿度、能见度）的科学关联
- 熟悉户外应用的用户体验设计
- 了解社交功能（点赞、评论、分享）的实现模式

### 工作风格

- 代码简洁、可读性强、注释完整
- 遵循SOLID原则和Clean Architecture
- 注重错误处理和边界情况
- 优先考虑性能和用户体验
- **输出完整可运行代码，绝不使用任何占位符或省略**

---

## R - Request（请求/任务）

### 核心任务

**一次性输出**一款功能完整的**钓鱼天气应用（Fishing Weather App）**的**全部代码**，包括前端、后端、数据库、测试。这是一款面向钓鱼爱好者的综合性移动应用。

### 功能需求（必须全部实现）

#### 模块1: 天气与钓鱼适宜度功能 ✅必须

- [x] 通过IP定位自动获取当前位置的天气和钓鱼适宜度
- [x] 支持GPS精确定位获取天气信息
- [x] 支持城市搜索查询天气
- [x] 显示未来3-7天天气预报和钓鱼适宜度
- [x] 根据天气条件提供详细钓鱼建议
- [x] 实现8项气象因素评分算法

#### 模块2: 用户认证功能 ✅必须

- [x] 邮箱注册和登录
- [x] JWT认证机制
- [x] 个人资料管理
- [x] 密码修改和找回

#### 模块3: 钓点分享功能 ✅必须

- [x] 创建钓点（位置、名称、描述、标签）
- [x] 按距离/名称查询钓点
- [x] 在地图上显示钓点分布
- [x] 删除自己的钓点

#### 模块4: 鱼获分享功能 ✅必须

- [x] 上传鱼获照片和描述
- [x] 社区feed展示
- [x] 点赞和评论功能

#### 模块5: 地图功能 ✅必须

- [x] 地图显示钓点标记
- [x] 支持缩放、平移、点击交互
- [x] 地图上直接添加新钓点

#### 模块6: 设置功能 ✅必须

- [x] 中英文切换
- [x] 离线缓存
- [x] 主题设置

---

## I - Input（输入/背景信息）

### 技术栈要求

```yaml
前端:
  框架: Flutter
  状态管理: Provider
  网络请求: http
  本地存储: shared_preferences
  地图组件: flutter_map
  图片处理: image_picker

后端:
  框架: FastAPI
  数据库: MySQL
  认证: JWT
  API设计: RESTful
  文件存储: 本地文件系统

天气API:
  主要: wttr.in (JSON格式)
  备选: OpenWeatherMap One Call API 3.0
```

### 钓鱼适宜度评估算法（必须完整实现）

```python
# 8项气象因素评分规则 - 必须完整实现此算法
class FishingScoreCalculator:
    """钓鱼适宜度计算器 - 基于8项气象因素"""

    SCORING_RULES = {
        "pressure": {  # 气压 (hPa)
            "optimal": (1005, 1015, 2),   # 最佳范围 +2分
            "good": (1015, 1025, 1),      # 良好 +1分
            "poor": (0, 1005, -1)         # 较差 -1分
        },
        "weather": {  # 天气状况
            "sunny": 2,           # 晴好天气 +2分
            "cloudy": 1,          # 多云 +1分
            "light_rain": 0,      # 小雨 0分
            "fog": -1,            # 雾 -1分
            "heavy_rain": -2      # 大雨 -2分
        },
        "precipitation": {  # 降水概率 (%)
            "low": (0, 30, 2),      # <30% +2分
            "medium": (30, 60, 0),  # 30-60% 0分
            "high": (60, 100, -1)   # >60% -1分
        },
        "cloud": {  # 云量 (%)
            "optimal": (20, 60, 2),    # 20-60% +2分
            "acceptable": (0, 80, 0),  # <20%或60-80% 0分
            "poor": (80, 100, -1)      # >80% -1分
        },
        "wind": {  # 风速 (km/h)
            "optimal": (2, 10, 2),     # 2-10 +2分
            "acceptable": (0, 15, 0),  # <2或10-15 0分
            "poor": (15, 100, -2)      # >15 -2分
        },
        "temperature": {  # 温度 (°C)
            "optimal": (15, 30, 2),    # 15-30 +2分
            "acceptable": (10, 35, 0), # <15或30-35 0分
            "extreme": (-50, 50, -2)   # 极端温度 -2分
        },
        "humidity": {  # 湿度 (%)
            "optimal": (40, 80, 2),    # 40-80% +2分
            "acceptable": (30, 90, 0), # <40%或80-90% 0分
            "poor": (90, 100, -1)      # >90% -1分
        },
        "visibility": {  # 能见度 (km)
            "good": (5, 100, 2),   # >5km +2分
            "medium": (2, 5, 0),   # 2-5km 0分
            "poor": (0, 2, -2)     # <2km -2分
        }
    }

    GRADE_LEVELS = {
        "excellent": {"min": 12, "color": "green", "label": "极佳"},
        "good": {"min": 8, "max": 11, "color": "blue", "label": "良好"},
        "moderate": {"min": 4, "max": 7, "color": "orange", "label": "一般"},
        "poor": {"max": 3, "color": "red", "label": "较差"}
    }

    def calculate_score(self, weather_data: dict) -> dict:
        """计算钓鱼适宜度分数 - 必须完整实现"""
        # 完整实现评分逻辑...
        pass  # ❌ 禁止：必须替换为完整实现

    def get_grade(self, score: int) -> dict:
        """根据分数获取等级 - 必须完整实现"""
        # 完整实现等级判断逻辑...
        pass  # ❌ 禁止：必须替换为完整实现

    def get_advice(self, score: int, weather_data: dict) -> str:
        """生成钓鱼建议 - 必须完整实现"""
        # 完整实现建议生成逻辑...
        pass  # ❌ 禁止：必须替换为完整实现
```

### 性能要求

- 应用启动时间: <3秒
- 天气数据加载: <2秒
- 地图加载: <3秒
- 图片上传: <5秒
- 支持离线模式显示缓存数据

### 兼容性要求

- Android 5.0+
- iOS 11.0+
- 适配不同屏幕尺寸
- 支持横屏/竖屏

---

## S - Style（风格/格式）

### 代码风格

- **语言**: Dart (Flutter) + Python (FastAPI)
- **命名规范**:
  - Dart: camelCase变量，PascalCase类名
  - Python: snake_case变量和函数，PascalCase类名
- **注释**: 关键函数必须有docstring，复杂逻辑需行内注释
- **文件组织**: 按功能模块分目录

### 输出格式

请按以下结构输出完整代码：

```
1. 项目结构
   - 目录树
   - 各模块说明

2. 后端代码（FastAPI）- 必须完整
   - main.py（完整入口）
   - 所有路由文件（完整API实现）
   - 所有模型文件（完整数据模型）
   - 所有服务文件（完整业务逻辑）

3. 前端代码（Flutter）- 必须完整
   - main.dart（完整入口）
   - 所有页面文件（完整UI实现）
   - 所有服务文件（完整API调用）
   - 所有组件文件（完整Widget实现）

4. 数据库设计
   - 完整建表SQL
   - 索引和约束

5. 测试代码 - 必须完整
   - 单元测试
   - 集成测试

6. 功能完整性检查表
```

### 交付标准

- 代码可直接运行，禁止使用占位符
- 包含完整错误处理
- **包含完整的测试用例**（覆盖核心功能和边界情况）
- 代码有完整注释
- **完成后必须输出功能完整性检查表**
- **完成后必须输出测试报告**

### 禁止行为（严格执行）

```
❌ 禁止: # TODO: 实现...
❌ 禁止: # 此处省略...
❌ 禁止: pass  # 空函数体
❌ 禁止: raise NotImplementedError()
❌ 禁止: // ... 其他类似代码
❌ 禁止: 中途停止输出
```

---

## P - Process（流程/步骤）

请严格按照以下步骤执行，每个步骤必须输出完整代码：

### 步骤1: 项目初始化

1. 创建Flutter项目结构（输出完整目录结构）
2. 配置pubspec.yaml依赖（输出完整配置）
3. 创建FastAPI后端项目结构（输出完整目录结构）
4. 配置数据库连接（输出完整配置）

### 步骤2: 实现天气模块（必须完整）

1. 封装wttr.in API调用（完整HTTP请求代码）
2. 实现IP定位和GPS定位（完整定位代码）
3. 实现钓鱼适宜度评估算法（完整8因素评分代码）
4. 实现天气数据缓存机制（完整缓存代码）
5. 创建天气展示UI（完整Widget代码）

### 步骤3: 实现用户认证模块（必须完整）

1. 设计用户数据表（完整SQL）
2. 实现注册/登录API（完整FastAPI路由）
3. 实现JWT认证中间件（完整认证代码）
4. 创建登录/注册UI（完整Flutter页面）
5. 实现登录状态持久化（完整存储代码）

### 步骤4: 实现钓点模块（必须完整）

1. 设计钓点数据表（完整SQL）
2. 实现钓点CRUD API（完整FastAPI路由）
3. 集成flutter_map（完整地图代码）
4. 创建钓点列表和地图UI（完整Flutter页面）
5. 实现钓点搜索功能（完整搜索代码）

### 步骤5: 实现鱼获模块（必须完整）

1. 设计鱼获和互动数据表（完整SQL）
2. 实现鱼获CRUD API（完整FastAPI路由）
3. 实现点赞/评论功能（完整互动代码）
4. 创建社区feed UI（完整Flutter页面）
5. 实现图片上传功能（完整上传代码）

### 步骤6: 实现设置模块（必须完整）

1. 实现多语言切换（完整i18n代码）
2. 实现离线缓存逻辑（完整缓存代码）
3. 实现主题设置（完整主题代码）

### 步骤7: 测试与验证（必须完整）

1. **编写完整测试用例**
   - 单元测试：覆盖所有核心函数和方法
   - 集成测试：覆盖API接口调用链路
   - 边界测试：覆盖异常输入和极端情况
2. **输出功能完整性检查表**
3. **输出测试报告**

---

## E - Expectation（期望/输出标准）

### 期望输出

#### 1. Flutter项目结构（必须全部实现）

```
lib/
├── main.dart                      # 应用入口 ✅必须完整
├── config/
│   ├── app_config.dart           # 应用配置 ✅必须完整
│   ├── routes.dart               # 路由配置 ✅必须完整
│   └── theme.dart                # 主题配置 ✅必须完整
├── models/
│   ├── weather_model.dart        # 天气模型 ✅必须完整
│   ├── user_model.dart           # 用户模型 ✅必须完整
│   ├── fishing_spot_model.dart   # 钓点模型 ✅必须完整
│   └── catch_model.dart          # 鱼获模型 ✅必须完整
├── services/
│   ├── api_service.dart          # API基础服务 ✅必须完整
│   ├── weather_service.dart      # 天气服务 ✅必须完整
│   ├── auth_service.dart         # 认证服务 ✅必须完整
│   ├── spot_service.dart         # 钓点服务 ✅必须完整
│   ├── catch_service.dart        # 鱼获服务 ✅必须完整
│   └── storage_service.dart      # 存储服务 ✅必须完整
├── providers/
│   ├── weather_provider.dart     # 天气状态 ✅必须完整
│   ├── auth_provider.dart        # 认证状态 ✅必须完整
│   ├── spot_provider.dart        # 钓点状态 ✅必须完整
│   ├── catch_provider.dart       # 鱼获状态 ✅必须完整
│   └── locale_provider.dart      # 语言状态 ✅必须完整
├── screens/
│   ├── splash_screen.dart        # 启动页 ✅必须完整
│   ├── home_screen.dart          # 首页 ✅必须完整
│   ├── auth/
│   │   ├── login_screen.dart     # 登录页 ✅必须完整
│   │   └── register_screen.dart  # 注册页 ✅必须完整
│   ├── weather/
│   │   ├── weather_detail.dart   # 天气详情 ✅必须完整
│   │   └── forecast_screen.dart  # 预报页 ✅必须完整
│   ├── spots/
│   │   ├── spots_list.dart       # 钓点列表 ✅必须完整
│   │   ├── spot_detail.dart      # 钓点详情 ✅必须完整
│   │   └── add_spot.dart         # 添加钓点 ✅必须完整
│   ├── catches/
│   │   ├── catches_feed.dart     # 鱼获Feed ✅必须完整
│   │   ├── catch_detail.dart     # 鱼获详情 ✅必须完整
│   │   └── add_catch.dart        # 添加鱼获 ✅必须完整
│   ├── map/
│   │   └── map_screen.dart       # 地图页 ✅必须完整
│   ├── profile/
│   │   ├── profile_screen.dart   # 个人资料 ✅必须完整
│   │   └── edit_profile.dart     # 编辑资料 ✅必须完整
│   └── settings/
│       └── settings_screen.dart  # 设置页 ✅必须完整
├── widgets/
│   ├── weather_card.dart         # 天气卡片 ✅必须完整
│   ├── fishing_score_widget.dart # 评分组件 ✅必须完整
│   ├── spot_card.dart            # 钓点卡片 ✅必须完整
│   ├── catch_card.dart           # 鱼获卡片 ✅必须完整
│   └── common/
│       ├── loading_widget.dart   # 加载组件 ✅必须完整
│       ├── error_widget.dart     # 错误组件 ✅必须完整
│       └── empty_widget.dart     # 空状态组件 ✅必须完整
├── utils/
│   ├── fishing_calculator.dart   # 钓鱼评分 ✅必须完整
│   ├── cache_manager.dart        # 缓存管理 ✅必须完整
│   ├── validators.dart           # 表单验证 ✅必须完整
│   └── constants.dart            # 常量定义 ✅必须完整
└── l10n/
    ├── app_en.arb                # 英文 ✅必须完整
    └── app_zh.arb                # 中文 ✅必须完整
```

#### 2. FastAPI项目结构（必须全部实现）

```
backend/
├── main.py                       # 入口文件 ✅必须完整
├── config.py                     # 配置管理 ✅必须完整
├── database.py                   # 数据库连接 ✅必须完整
├── models/
│   ├── __init__.py
│   ├── user.py                   # 用户模型 ✅必须完整
│   ├── spot.py                   # 钓点模型 ✅必须完整
│   └── catch.py                  # 鱼获模型 ✅必须完整
├── schemas/
│   ├── __init__.py
│   ├── user.py                   # 用户Schema ✅必须完整
│   ├── spot.py                   # 钓点Schema ✅必须完整
│   ├── catch.py                  # 鱼获Schema ✅必须完整
│   └── weather.py                # 天气Schema ✅必须完整
├── routers/
│   ├── __init__.py
│   ├── auth.py                   # 认证路由 ✅必须完整
│   ├── users.py                  # 用户路由 ✅必须完整
│   ├── weather.py                # 天气路由 ✅必须完整
│   ├── spots.py                  # 钓点路由 ✅必须完整
│   └── catches.py                # 鱼获路由 ✅必须完整
├── services/
│   ├── __init__.py
│   ├── auth_service.py           # 认证服务 ✅必须完整
│   ├── weather_service.py        # 天气服务 ✅必须完整
│   ├── fishing_score.py          # 评分服务 ✅必须完整
│   └── file_service.py           # 文件服务 ✅必须完整
├── utils/
│   ├── __init__.py
│   ├── security.py               # 安全工具 ✅必须完整
│   └── dependencies.py           # 依赖注入 ✅必须完整
├── tests/
│   ├── __init__.py
│   ├── test_auth.py              # 认证测试 ✅必须完整
│   ├── test_weather.py           # 天气测试 ✅必须完整
│   ├── test_spots.py             # 钓点测试 ✅必须完整
│   └── test_catches.py           # 鱼获测试 ✅必须完整
└── requirements.txt              # 依赖配置 ✅必须完整
```

#### 3. 数据库表结构（必须完整）

```sql
-- 用户表
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nickname VARCHAR(100),
    avatar_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email)
);

-- 钓点表
CREATE TABLE fishing_spots (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    tags JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_location (latitude, longitude)
);

-- 鱼获表
CREATE TABLE catches (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    image_url VARCHAR(500) NOT NULL,
    description TEXT,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    tags JSON,
    likes_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_created_at (created_at)
);

-- 互动表
CREATE TABLE interactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    catch_id INT NOT NULL,
    type ENUM('like', 'comment') NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (catch_id) REFERENCES catches(id) ON DELETE CASCADE,
    UNIQUE KEY unique_like (user_id, catch_id, type),
    INDEX idx_catch_id (catch_id)
);
```

#### 4. 核心API接口（必须全部实现）

```
认证模块（必须完整实现）:
POST /api/auth/register    - 用户注册 ✅
POST /api/auth/login       - 用户登录 ✅
POST /api/auth/refresh     - 刷新Token ✅
GET  /api/auth/profile     - 获取个人资料 ✅
PUT  /api/auth/profile     - 更新个人资料 ✅
PUT  /api/auth/password    - 修改密码 ✅

天气模块（必须完整实现）:
GET  /api/weather/current      - 获取当前天气 ✅
GET  /api/weather/forecast     - 获取天气预报 ✅
GET  /api/weather/fishing-score - 获取钓鱼适宜度 ✅
GET  /api/weather/search       - 搜索城市天气 ✅

钓点模块（必须完整实现）:
GET    /api/spots          - 获取钓点列表 ✅
POST   /api/spots          - 创建钓点 ✅
GET    /api/spots/:id      - 获取钓点详情 ✅
DELETE /api/spots/:id      - 删除钓点 ✅
GET    /api/spots/nearby   - 获取附近钓点 ✅

鱼获模块（必须完整实现）:
GET    /api/catches            - 获取鱼获列表 ✅
POST   /api/catches            - 创建鱼获 ✅
GET    /api/catches/:id        - 获取鱼获详情 ✅
DELETE /api/catches/:id        - 删除鱼获 ✅
POST   /api/catches/:id/like   - 点赞 ✅
DELETE /api/catches/:id/like   - 取消点赞 ✅
POST   /api/catches/:id/comment - 评论 ✅
GET    /api/catches/:id/comments - 获取评论列表 ✅
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
║ 天气模块          │ IP定位获取天气           │ ✅/❌        ║
║                   │ GPS定位获取天气          │ ✅/❌        ║
║                   │ 城市搜索                  │ ✅/❌        ║
║                   │ 钓鱼评分算法(8因素)      │ ✅/❌        ║
║                   │ 7天预报                   │ ✅/❌        ║
║                   │ 钓鱼建议                  │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 用户认证          │ 邮箱注册                  │ ✅/❌        ║
║                   │ 邮箱登录                  │ ✅/❌        ║
║                   │ JWT认证                   │ ✅/❌        ║
║                   │ Token刷新                 │ ✅/❌        ║
║                   │ 个人资料管理              │ ✅/❌        ║
║                   │ 密码修改                  │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 钓点模块          │ 创建钓点                  │ ✅/❌        ║
║                   │ 查询钓点(距离/名称)       │ ✅/❌        ║
║                   │ 删除钓点                  │ ✅/❌        ║
║                   │ 地图显示钓点              │ ✅/❌        ║
║                   │ 附近钓点查询              │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 鱼获模块          │ 上传鱼获(图片+描述)       │ ✅/❌        ║
║                   │ Feed展示                  │ ✅/❌        ║
║                   │ 点赞功能                  │ ✅/❌        ║
║                   │ 取消点赞                  │ ✅/❌        ║
║                   │ 评论功能                  │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 地图模块          │ 地图显示                  │ ✅/❌        ║
║                   │ 地图交互(缩放/平移)       │ ✅/❌        ║
║                   │ 地图添加钓点              │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 设置模块          │ 中英文切换                │ ✅/❌        ║
║                   │ 离线缓存                  │ ✅/❌        ║
║                   │ 主题设置                  │ ✅/❌        ║
╠══════════════════════════════════════════════════════════════╣
║ 代码质量          │ 无TODO占位符              │ ✅/❌        ║
║                   │ 无省略代码                │ ✅/❌        ║
║                   │ 所有函数完整实现          │ ✅/❌        ║
║                   │ 错误处理完整              │ ✅/❌        ║
║                   │ 测试用例输出              │ ✅/❌        ║
╚══════════════════════════════════════════════════════════════╝

总计: XX/35 项完成
完成率: XX%
```

---

## 🧪 测试报告（必须在最后输出）

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
║    ✅ test_weather_cache                                      ║
║                                                               ║
║ 2. 用户认证模块 [X/Y 通过]                                    ║
║    ✅ test_user_register_success                              ║
║    ✅ test_user_register_duplicate                            ║
║    ✅ test_user_login_success                                 ║
║    ✅ test_user_login_wrong_password                          ║
║    ✅ test_jwt_validation                                     ║
║    ✅ test_jwt_refresh                                        ║
║    ✅ test_jwt_expired                                        ║
║                                                               ║
║ 3. 钓点模块 [X/Y 通过]                                        ║
║    ✅ test_create_spot_success                                ║
║    ✅ test_create_spot_invalid                                ║
║    ✅ test_query_spots_by_distance                            ║
║    ✅ test_query_spots_by_name                                ║
║    ✅ test_delete_own_spot                                    ║
║    ✅ test_delete_other_spot_forbidden                        ║
║                                                               ║
║ 4. 鱼获模块 [X/Y 通过]                                        ║
║    ✅ test_upload_catch                                       ║
║    ✅ test_like_catch                                         ║
║    ✅ test_unlike_catch                                       ║
║    ✅ test_comment_catch                                      ║
║    ✅ test_feed_pagination                                    ║
║                                                               ║
║ 5. 边界情况测试 [X/Y 通过]                                    ║
║    ✅ test_empty_data_handling                                ║
║    ✅ test_invalid_input_validation                           ║
║    ✅ test_network_error_recovery                             ║
║    ✅ test_concurrent_requests                                ║
╠═══════════════════════════════════════════════════════════════╣
║ ❌ 失败用例详情（如有）                                        ║
║ [列出失败的测试用例及错误信息]                                  ║
╠═══════════════════════════════════════════════════════════════╣
║ 📝 测试结论                                                    ║
║ [总体评估和建议]                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## ✅ 成功标准

- [ ] 所有35项功能全部实现（检查表全部✅）
- [ ] 钓鱼适宜度算法准确计算（8因素评分）
- [ ] 用户认证流程完整（注册/登录/JWT）
- [ ] 地图功能正常显示和交互
- [ ] 离线缓存机制有效
- [ ] 性能指标达标
- [ ] 代码无TODO、无占位符、无省略
- [ ] **测试用例覆盖率 ≥ 80%**
- [ ] **所有测试用例通过**
- [ ] **功能完整性检查表已输出**
- [ ] **测试报告已输出**

---

## 📝 使用说明

将此提示词发送给AI，将获得：

1. ✅ 完整的后端API代码（FastAPI，所有端点可运行）
2. ✅ 完整的前端代码（Flutter，所有页面可渲染）
3. ✅ 完整的数据库模型和建表SQL
4. ✅ 完整的测试用例（单元测试+集成测试）
5. ✅ 功能完整性检查表（确认所有功能已实现）
6. ✅ 测试执行报告

---

## ⚡ 快速开始提示

如需快速获取完整代码，可直接发送：

```
请根据上述CRISPE框架提示词，一次性输出钓鱼天气应用的完整代码。
要求：
1. 输出所有后端FastAPI代码（完整可运行）
2. 输出所有前端Flutter代码（完整可运行）
3. 输出所有测试代码
4. 最后输出功能完整性检查表（35项）
5. 最后输出测试报告
6. 禁止使用TODO、禁止省略代码、所有函数必须完整实现
```
