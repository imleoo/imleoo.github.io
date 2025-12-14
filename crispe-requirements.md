# 钓鱼天气应用 - CRISPE框架提示词

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

---

## R - Request（请求/任务）

### 核心任务
开发一款**钓鱼天气应用（Fishing Weather App）**，这是一款面向钓鱼爱好者的综合性移动应用，需要实现以下功能：

### 功能需求

#### 1. 天气与钓鱼适宜度功能
- 通过IP定位自动获取当前位置的天气和钓鱼适宜度
- 支持GPS精确定位获取天气信息
- 支持城市搜索查询天气
- 显示未来3-7天天气预报和钓鱼适宜度
- 根据天气条件提供详细钓鱼建议

#### 2. 用户认证功能
- 邮箱注册和登录
- JWT认证机制
- 个人资料管理
- 密码修改和找回

#### 3. 钓点分享功能
- 创建钓点（位置、名称、描述、标签）
- 按距离/名称查询钓点
- 在地图上显示钓点分布
- 删除自己的钓点

#### 4. 鱼获分享功能
- 上传鱼获照片和描述
- 社区feed展示
- 点赞和评论功能

#### 5. 地图功能
- 地图显示钓点标记
- 支持缩放、平移、点击交互
- 地图上直接添加新钓点

#### 6. 设置功能
- 中英文切换
- 离线缓存
- 主屏幕小部件

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

### 钓鱼适宜度评估算法

```python
# 8项气象因素评分规则
评分因素 = {
    "气压": {
        "1005-1015 hPa": +2,
        ">1015 hPa": +1,
        "<1005 hPa": -1
    },
    "天气状况": {
        "晴好天气": +2,
        "小雨/零星降雨": 0,
        "雾/薄雾": -1,
        "大雨/恶劣天气": -2
    },
    "降水概率": {
        "<30%": +2,
        "30-60%": 0,
        ">60%": -1
    },
    "云量": {
        "20-60%": +2,
        "<20% 或 60-80%": 0,
        ">80%": -1
    },
    "风速": {
        "2-10 km/h": +2,
        "<2 或 10-15 km/h": 0,
        ">15 km/h": -2
    },
    "温度": {
        "15-30°C": +2,
        "<15°C 或 30-35°C": 0,
        ">35°C 或极低温": -2
    },
    "湿度": {
        "40-80%": +2,
        "<40% 或 80-90%": 0,
        ">90%": -1
    },
    "能见度": {
        ">5km": +2,
        "2-5km": 0,
        "<2km": -2
    }
}

# 适宜度等级
等级 = {
    "极佳(Excellent)": "≥12分, 绿色",
    "良好(Good)": "8-11分, 蓝色",
    "一般(Moderate)": "4-7分, 橙色",
    "较差(Poor)": "<4分, 红色"
}
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
请按以下结构输出：

```
1. 项目结构
   - 目录树
   - 各模块说明

2. 核心代码
   - 按模块分组
   - 包含完整注释

3. 数据库设计
   - ER图描述
   - 建表SQL

4. API文档
   - 接口列表
   - 请求/响应示例

5. 使用说明
   - 环境配置
   - 运行步骤
```

### 交付标准
- 代码可直接运行
- 包含错误处理
- **包含完整的测试用例**（覆盖核心功能和边界情况）
- 代码有完整注释
- **完成后必须输出测试报告**

---

## P - Process（流程/步骤）

请严格按照以下步骤执行：

### 步骤1: 项目初始化
1. 创建Flutter项目结构
2. 配置pubspec.yaml依赖
3. 创建FastAPI后端项目结构
4. 配置数据库连接

### 步骤2: 实现天气模块
1. 封装wttr.in API调用
2. 实现IP定位和GPS定位
3. 实现钓鱼适宜度评估算法
4. 实现天气数据缓存机制
5. 创建天气展示UI

### 步骤3: 实现用户认证模块
1. 设计用户数据表
2. 实现注册/登录API
3. 实现JWT认证中间件
4. 创建登录/注册UI
5. 实现登录状态持久化

### 步骤4: 实现钓点模块
1. 设计钓点数据表
2. 实现钓点CRUD API
3. 集成flutter_map
4. 创建钓点列表和地图UI
5. 实现钓点搜索功能

### 步骤5: 实现鱼获模块
1. 设计鱼获和互动数据表
2. 实现鱼获CRUD API
3. 实现点赞/评论功能
4. 创建社区feed UI
5. 实现图片上传功能

### 步骤6: 实现设置模块
1. 实现多语言切换
2. 实现离线缓存逻辑
3. 实现主屏幕小部件（iOS/Android）

### 步骤7: 测试与优化
1. **编写完整测试用例**
   - 单元测试：覆盖所有核心函数和方法
   - 集成测试：覆盖API接口调用链路
   - 边界测试：覆盖异常输入和极端情况
2. **执行测试并生成测试报告**
   - 运行所有测试用例
   - 记录测试结果（通过/失败/跳过）
   - 统计测试覆盖率
3. 进行性能测试
4. 优化加载速度
5. 处理边界情况

---

## E - Expectation（期望/输出标准）

### 期望输出

#### 1. Flutter项目结构
```
lib/
├── main.dart
├── config/
│   ├── app_config.dart
│   └── routes.dart
├── models/
│   ├── weather_model.dart
│   ├── user_model.dart
│   ├── fishing_spot_model.dart
│   └── catch_model.dart
├── services/
│   ├── weather_service.dart
│   ├── auth_service.dart
│   ├── spot_service.dart
│   └── catch_service.dart
├── providers/
│   ├── weather_provider.dart
│   ├── auth_provider.dart
│   └── app_provider.dart
├── screens/
│   ├── home/
│   ├── auth/
│   ├── map/
│   ├── community/
│   └── profile/
├── widgets/
│   ├── weather_card.dart
│   ├── fishing_score_widget.dart
│   └── spot_marker.dart
└── utils/
    ├── fishing_calculator.dart
    ├── cache_manager.dart
    └── constants.dart
```

#### 2. FastAPI项目结构
```
backend/
├── main.py
├── config.py
├── database.py
├── models/
│   ├── user.py
│   ├── spot.py
│   └── catch.py
├── schemas/
│   ├── user.py
│   ├── spot.py
│   └── catch.py
├── routers/
│   ├── auth.py
│   ├── weather.py
│   ├── spots.py
│   └── catches.py
├── services/
│   ├── weather_service.py
│   └── auth_service.py
└── utils/
    ├── security.py
    └── fishing_calculator.py
```

#### 3. 数据库表结构
```sql
-- 用户表
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nickname VARCHAR(100),
    avatar_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    FOREIGN KEY (user_id) REFERENCES users(id)
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
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- 互动表
CREATE TABLE interactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    catch_id INT NOT NULL,
    type ENUM('like', 'comment') NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (catch_id) REFERENCES catches(id)
);
```

#### 4. 核心API接口
```
认证模块:
POST /api/auth/register    - 用户注册
POST /api/auth/login       - 用户登录
GET  /api/auth/profile     - 获取个人资料
PUT  /api/auth/profile     - 更新个人资料

天气模块:
GET  /api/weather/current  - 获取当前天气
GET  /api/weather/forecast - 获取天气预报
GET  /api/weather/fishing-score - 获取钓鱼适宜度

钓点模块:
GET    /api/spots          - 获取钓点列表
POST   /api/spots          - 创建钓点
GET    /api/spots/:id      - 获取钓点详情
DELETE /api/spots/:id      - 删除钓点

鱼获模块:
GET    /api/catches        - 获取鱼获列表
POST   /api/catches        - 创建鱼获
POST   /api/catches/:id/like    - 点赞
POST   /api/catches/:id/comment - 评论
```

#### 5. 测试用例
```
测试用例结构:
├── test/
│   ├── unit/                      # 单元测试
│   │   ├── fishing_calculator_test.dart
│   │   ├── weather_service_test.dart
│   │   └── auth_service_test.dart
│   ├── integration/               # 集成测试
│   │   ├── api_integration_test.dart
│   │   └── database_test.py
│   └── backend/                   # 后端测试
│       ├── test_auth.py
│       ├── test_weather.py
│       ├── test_spots.py
│       └── test_catches.py

必须覆盖的测试场景:
- 钓鱼适宜度计算：各种气象条件组合
- 用户认证：注册、登录、Token验证、过期处理
- 钓点操作：创建、查询、删除、权限验证
- 鱼获互动：上传、点赞、评论、取消
- 边界情况：空数据、无效输入、网络异常
```

#### 6. 测试报告
完成所有开发后，必须输出以下格式的测试报告：

```
================== 测试报告 ==================

📅 测试时间: [YYYY-MM-DD HH:MM:SS]
📦 项目名称: 钓鱼天气应用
🔧 测试环境: [环境信息]

────────────────────────────────────────────
📊 测试概览
────────────────────────────────────────────
| 指标         | 数值    |
|-------------|--------|
| 总用例数     | XX     |
| 通过         | XX ✅  |
| 失败         | XX ❌  |
| 跳过         | XX ⏭️  |
| 通过率       | XX%    |
| 覆盖率       | XX%    |

────────────────────────────────────────────
📋 模块测试详情
────────────────────────────────────────────

1. 天气模块 [X/Y 通过]
   ✅ test_weather_api_call
   ✅ test_fishing_score_calculation
   ✅ test_weather_cache
   ...

2. 用户认证模块 [X/Y 通过]
   ✅ test_user_register
   ✅ test_user_login
   ✅ test_jwt_validation
   ...

3. 钓点模块 [X/Y 通过]
   ✅ test_create_spot
   ✅ test_query_spots
   ...

4. 鱼获模块 [X/Y 通过]
   ✅ test_upload_catch
   ✅ test_like_catch
   ...

5. 边界情况测试 [X/Y 通过]
   ✅ test_invalid_input
   ✅ test_network_error
   ...

────────────────────────────────────────────
❌ 失败用例详情（如有）
────────────────────────────────────────────
[列出失败的测试用例及错误信息]

────────────────────────────────────────────
📝 测试结论
────────────────────────────────────────────
[总体评估和建议]

==============================================
```

### 成功标准
- [ ] 所有功能模块可正常运行
- [ ] 钓鱼适宜度算法准确计算
- [ ] 用户认证流程完整
- [ ] 地图功能正常显示
- [ ] 离线缓存机制有效
- [ ] 性能指标达标
- [ ] 代码注释完整
- [ ] **测试用例覆盖率 ≥ 80%**
- [ ] **所有测试用例通过**
- [ ] **测试报告已输出**

---

## 使用说明

将此提示词发送给AI，AI将按照CRISPE框架的六个要素，系统化地完成钓鱼天气应用的开发任务，输出完整的项目代码和文档。
