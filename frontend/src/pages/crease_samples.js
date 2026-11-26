        import {workspace} from '../workspace.js';
        import {el} from '../dom.js';

        const page = {
  "title": "原位观察折痕",
  "module": "折痕样条",
  "caption": "折痕样条",
  "detail": "登记已经形成的折痕。借出旗面须先归还才能完成样条确认。",
  "path": "/crease_samples",
  "columns": [
    {
      "name": "code",
      "label": "编号"
    },
    {
      "name": "flag",
      "label": "旗面"
    },
    {
      "name": "depth",
      "label": "平均折深 mm"
    },
    {
      "name": "width",
      "label": "折距 mm"
    },
    {
      "name": "lines",
      "label": "平行线数"
    },
    {
      "name": "signed",
      "label": "图样已核对"
    }
  ],
  "layout": "stack",
  "view": "table",
  "actions": [
    {
      "name": "capture_crease",
      "label": "抄录折痕样条",
      "path": "/crease_samples/capture-crease",
      "fields": [
        {
          "name": "code",
          "label": "样条号",
          "kind": "text",
          "initial": "CK-NEW"
        },
        {
          "name": "flag",
          "label": "旗面号",
          "kind": "text",
          "initial": "FLAG-A1"
        },
        {
          "name": "depth",
          "label": "折深 mm",
          "kind": "float",
          "initial": 3.12
        },
        {
          "name": "width",
          "label": "折距 mm",
          "kind": "float",
          "initial": 10.1
        },
        {
          "name": "lines",
          "label": "平行线数",
          "kind": "int",
          "initial": 5
        }
      ],
      "help": "以现有折痕为依据录入读数。",
      "roles": [
        "operator",
        "reviewer"
      ],
      "success": "已写入"
    },
    {
      "name": "verify_crease",
      "label": "签认照片与折痕记录",
      "path": "/crease_samples/verify-crease",
      "fields": [
        {
          "name": "sample",
          "label": "样条号",
          "kind": "text",
          "initial": "CK-NEW"
        }
      ],
      "help": "由藏品复核员确认样条。",
      "roles": [
        "reviewer"
      ],
      "success": "已写入"
    }
  ]
};

        export const {title} = page;
        export const key = "crease_samples";
        export async function render(root, role) {
          await workspace(root, role, page);

        }
