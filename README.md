# 城市典礼旗面布褶归档

槐语保障科记录旗面的原有折痕，从旧例挑选相近代表样，替班交接时管住礼藏原件的处置权限。

## 现场工作与联系人

模拟客户为槐语庆典保障科。仪典旗面、归档折痕样、代表样簇、折叠教程替班复核；遗产旗不能重折，只标记特殊保管。

- 旗面与管护登记 `flag_archive`，字段为 `material`（面料）、`heritage`（礼藏原件）、`displayed`（仪典借出）。模型约束位于 `backend/domain/flag_archive_model.py`，规则位于 `flag_archive_service.py`。
- 折痕样条 `crease_samples`，字段为 `flag`（旗面）、`depth`（平均折深 mm）、`width`（折距 mm）、`lines`（平行线数）、`signed`（图样已核对）。模型约束位于 `backend/domain/crease_samples_model.py`，规则位于 `crease_samples_service.py`。
- 旗面折态代表样 `fold_exemplars`，字段为 `sample`（目标样条）、`example`（代表样）、`group_size`（折态簇样本数量）、`token`（计算号）。模型约束位于 `backend/domain/fold_exemplars_model.py`，规则位于 `fold_exemplars_service.py`。
- 礼具归档移交 `storage_slips`，字段为 `guide`（代表样凭据）、`flag`（旗面）、`action`（归档动作）、`locker`（保管柜）、`witness`（替班双签）。模型约束位于 `backend/domain/storage_slips_model.py`，规则位于 `storage_slips_service.py`。

团队为模拟的6 人典礼保障科，负责典礼旗布的归库和替班保管。

替班人员在旗面标签、折痕尺记和交班簿之间确认。折痕模板容易选错，遗产旗容易被当作普通旗处理，交接人到岗时间难对齐。

入库旗面核对和折痕样送入代表样检索，接班岗位签认平放、重折或特殊保管方式。

### 一天的业务操作

1. 08:40 FLAG-C3 礼宾归还。
2. 09:00 对 FLAG-A1 抄录折痕深 3.12 mm。
3. 10:40 签认照片与样条。
4. 13:00 使用 30 条旧样计算代表。
5. 14:00 保管员查看代表样后提出重折，礼藏约束拦截。
6. 15:30 刘敏与陈明按特殊保管移交 A-11。

## 启动

```sh
cp .env.example .env
docker compose up -d --build --wait
docker compose exec -T backend python -m scripts.seed_demo
```

打开 `http://127.0.0.1:18328`。FastAPI OpenAPI 在 `http://127.0.0.1:19328/docs`。
Compose 运行 Nginx、Python FastAPI、独立 Redis 消费进程、SQL 数据库和 Redis，SQL 与 Redis 使用命名卷。
本机开发时，在 Python 3.11 环境安装 `backend/requirements.txt` 后从 backend 目录运行 `uvicorn core.app:app`。须提供 `DATABASE_URL`、`REDIS_URL`、`JWT_SECRET`，`SEED_DEMO` 控制演示初始化。

| 演示账号 | 权限 |
|---|---|
| operator@demo.test | 提交领域记录和计算请求 |
| reviewer@demo.test | 提交记录并执行有业务约束的复核操作 |
| viewer@demo.test | 浏览业务台账 |

三个本地演示账号均使用 `DemoC0de!2026`。角色在 `backend/core/roles.py` 和 `frontend/src/store.js` 中声明。计算状态在 worker、queueing、API 和同一前端 store 中使用。

## 页面与接口

| 业务任务 | FastAPI 路由 | 页面 |
|---|---|---|
| 旗面与管护登记 | `/flag_archive` /flag_archive/return-flag | `frontend/src/pages/flag_archive.js` |
| 折痕样条 | `/crease_samples` /crease_samples/capture-crease，/crease_samples/verify-crease | `frontend/src/pages/crease_samples.js` |
| 旗面折态代表样 | `/fold_exemplars` /fold_exemplars/find-exemplar，/fold_exemplars/save-exemplar | `frontend/src/pages/fold_exemplars.js` |
| 礼具归档移交 | `/storage_slips` /storage_slips/handoff-flag | `frontend/src/pages/storage_slips.js` |

SQL 实体与约束在 `backend/domain` 下维护。前端使用原生 ES modules。核心算子为 AffinityPropagation。在标准化空间用 AffinityPropagation 搜索代表样，查询归入欧氏距离最近的代表簇。

旗面和读数为模拟记录。应用供文档移交使用，折痕样条无实际馆藏影像。

[MIT](LICENSE)
