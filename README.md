<h1 align="center">JetBrains Maple Mono</h1>
<h3 align="center">- JetBrains Mono + Maple Mono -</h3>
</br>

## 自我介绍
**JetBrains Maple Mono**: 一只基于 **Github Workflows (Bash)** 的 [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) + [Maple Mono](https://github.com/subframe7536/maple-font) 合成字体

* 适用平台: Any

## 字形特征
* 完美融合，Maple Mono 补充 JetBrains Mono 中日字形空缺
* 高可读性，等宽无衬线，中英文 2:1 宽完美对齐
* 丰富字重，智能连字，Nerd Font，Hints 原生支持
* 实时更新，构建合成优化发布全流程自动化

![Font Showcase](https://github.com/user-attachments/assets/6587588d-1a9d-4ee7-a0f9-8dd2e7f417e0)

## 下载地址
1. **Github (latest): [https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono/releases/latest](https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono/releases/latest)**
2. Github (preview): [https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono/releases/tag/pre](https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono/releases/tag/pre)

## 下载哪个
发布文件按 **JetBrainsMapleMono-[NF/XX]-[NR/XX]-[HT/XX].zip** 的格式命名:

1. XX: 占位符，表示该字体没有增加这一特性
2. NF: Nerd Font，为部分开发工具、命令行终端、代码编辑器等提供图标支持 (会导致字体文件体积略微增大)
3. NR: CN Narrow，缩小中日字体间距 (会导致 中英文 / 日英文 不再 2:1 宽完美对齐)
4. HT: Hinted，使字体在低分辨率屏幕上 (<=1080P) 的渲染更加均匀 (可能会导致字体在高分辨率屏幕上的渲染略微模糊)

> 如果依然不清楚如何选择请下载 **JetBrainsMapleMono-XX-XX-XX.zip**

## 注意事项
1. 如果在 Visual Studio 中使用本字体，请务必在 `设置 -> 文本编辑器 -> 高级` 中将 `文本格式设置方法` 设置为 `理想`，否则可能导致字体渲染不均匀
2. 如果需要在 VS Code 中启用连字，请在 `settings.json` 中添加以下配置 `"editor.fontLigatures": true`，反之删除

## CDN 托管
ZSFT: [https://fonts.zeoseven.com/items/521](https://fonts.zeoseven.com/items/521)

## 脚本流程
1. 每 5 - 30 分钟自动向上游 JetBrains Mono & Maple Mono 存储库**检查 Release 和 Commit 更新**

> 可手动选择跳过检查更新强制合成字体

2. 如有更新则**构建、合成字体，并执行一系列字体优化流程**

> 字体优化流程: 覆写元数据，设置锚点顺序，插入 Instr 和 Hint 信息，添加极值控制点，整理轮廓和起始点，清理冗余控制点，舍入控制点坐标，移除重叠路径

3. 如构建、合成、优化成功则**将字体发布到 Github Release** (Release 发布为 latest，Commit 发布在 preview)

> 完整执行一次脚本流程约需耗时 3h

## 实时监测
最近一次检查更新的时间:

* 北京时间: <!--BJT_TIME-->2025-10-31 05:42:18<!--BJT_TIME-->
* UTC 时间: <!--UTC_TIME-->2025-10-30 21:42:18<!--UTC_TIME-->

## 未来路线
1. 添加可变字重版本
2. 添加无连字版本
3. 直接基于资源圆体或思源黑体以获得更大的自定义空间，如自定义笔画末端弧度以及包含更多字符集等

## 致谢名单
* **JetBrains Mono: 为本项目提供所有非中日字形设计**
* **Maple Mono: 为本项目提供所有中日字形设计**
* **Resource Han Rounded: 为本项目提供所有中日基础字形设计**
* **Source Han Sans: 为本项目提供所有中日基础字形设计**

## 开发者
**Space Time**

## 联系方式
1. **邮箱: Zeus6_6@163.com**
2. 我的[其他项目](https://github.com/SpaceTimee/Sheas-Cealer)的 QQ 群: 1034315671，716266896，338919498

## 开源协议
[OFL-1.1](https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono?tab=OFL-1.1-1-ov-file)

•ᴗ•
