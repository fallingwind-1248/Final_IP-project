# 实际验证记录

记录日期为2026-10-15（Asia/Shanghai）。机器JSON中的Z时间为UTC，对应本地时间加八小时。

| 记录 | 结论 |
|---|---|
| environment/environment.json | Git、Node、Twine、Blender、Tweego、SugarCube及浏览器可用。 |
| environment/blender-render.json | 默认场景保存与1280×720 CPU渲染通过。 |
| environment/editor.json | 项目专用英文Twine编辑器及技术模板就绪。 |
| tests/source-check.json | 当前故事结构、链接目标和素材来源字段检查通过。 |
| tests/browser-tests.json | 两浏览器×三窗口，解压ZIP且网络禁用条件下的交互与音频状态检查通过。 |
| tests/twine-roundtrip.json | Twine真实导出、编译与重新导入，正文、节点及样式脚本一致。 |
| tests/author-text-check.json | 技术修改后的正文与交接点一致。 |
| tests/author-guard-regression.json | 技术编辑接受、正文变更拒绝、还原后接受三项通过。 |
| tests/package.json | 运行包白名单及文件哈希。 |

screenshots与blender-smoke中的大图和工程保留在本机，排除出Git。截图由自动化获得，不代表学生亲手操作。
manual-listening、second-computer和human-editor-trial保留待人工确认。
工具安装包、浏览器测试用户数据与临时导出不提交。失败历史与当前结果分别保存。
