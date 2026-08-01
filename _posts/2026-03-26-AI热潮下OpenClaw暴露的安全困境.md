---
layout: post
title: "AI热潮下OpenClaw暴露的安全困境"
date: 2026-03-26
article_id: 2646415
source: https://cloud.tencent.com/developer/article/2646415
---
# AI热潮下OpenClaw暴露的安全困境

OpenClaw 火起来以后，假安装包很快就跟上了。这次不是泛泛而谈：Huntress 记录了一台真实受感染的 Windows 设备。用户通过 Bing 的 AI 搜索结果进入伪造的 GitHub 仓库，运行所谓安装程序后，机器被投放了信息窃取软件。研究人员还发现了面向 macOS 的恶意下载链。

原稿只顾着说「这事儿挺有意思」，却没有把安全报告和感染过程写出来。安全新闻最怕这样，口气像亲眼看见，证据一个不留。

攻击方法其实很老：热门软件出来，攻击者做个长得很像的下载页，等着着急尝鲜的人自己运行。新东西在于搜索结果由 AI 推荐。用户不仅信 GitHub，也容易把 AI 给出的第一条链接当成答案，两个信任叠在一起，恶意仓库就穿上了官方外套。

开源不是问题，下载来源才是。官方仓库公开代码，不代表名字相似的 GitHub 组织也可信；搜索平台给出链接，也不等于平台替安装包做过安全审计。

普通用户能做的事不多，但很具体：从 OpenClaw 官网进入官方仓库，核对组织名和发布页，不运行搜索结果里来路不明的一键安装命令。做不到这些，就别在装着常用账号和密钥的机器上尝鲜。

参考：[Huntress：How Fake OpenClaw Installers Spread GhostSocks Malware](https://www.huntress.com/blog/openclaw-github-ghostsocks-infostealer)
