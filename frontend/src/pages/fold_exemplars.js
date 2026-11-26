        import {workspace} from '../workspace.js';
        import {el} from '../dom.js';

        const page = {
  "title": "代表样与归档比照",
  "module": "旗面折态代表样",
  "caption": "旗面折态代表样",
  "detail": "通过相似度消息传播选择相似折态，查看每个样簇的保管参考。",
  "path": "/fold_exemplars",
  "columns": [
    {
      "name": "code",
      "label": "编号"
    },
    {
      "name": "sample",
      "label": "目标样条"
    },
    {
      "name": "example",
      "label": "代表样"
    },
    {
      "name": "group_size",
      "label": "折态簇样本数量"
    },
    {
      "name": "token",
      "label": "计算号"
    },
    {
      "name": "version",
      "label": "模型版本"
    }
  ],
  "layout": "split",
  "view": "grid",
  "actions": [
    {
      "name": "find_exemplar",
      "label": "寻找折态代表样",
      "path": "/fold_exemplars/find-exemplar",
      "fields": [
        {
          "name": "sample",
          "label": "样条号",
          "kind": "text",
          "initial": "CK-NEW"
        }
      ],
      "help": "以已签认样条计算三项测量上的代表样。",
      "roles": [
        "operator",
        "reviewer"
      ],
      "success": "已写入"
    },
    {
      "name": "save_exemplar",
      "label": "把代表样写入参考册",
      "path": "/fold_exemplars/save-exemplar",
      "fields": [
        {
          "name": "code",
          "label": "折态参考号",
          "kind": "text",
          "initial": "REFERENCE-24"
        },
        {
          "name": "token",
          "label": "计算号",
          "kind": "token",
          "initial": ""
        }
      ],
      "help": "参考册附带可追踪的原样号。",
      "roles": [
        "reviewer"
      ],
      "success": "已写入"
    }
  ]
};

        export const {title} = page;
        export const key = "fold_exemplars";
        export async function render(root, role) {
          await workspace(root, role, page);

        }
