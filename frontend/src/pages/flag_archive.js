        import {workspace} from '../workspace.js';
        import {el} from '../dom.js';

        const page = {
  "title": "礼仪旗面的借归状态",
  "module": "旗面与管护登记",
  "caption": "旗面与管护登记",
  "detail": "借出状态与旗面分类直接约束取样与移交动作。",
  "path": "/flag_archive",
  "columns": [
    {
      "name": "code",
      "label": "编号"
    },
    {
      "name": "material",
      "label": "面料"
    },
    {
      "name": "heritage",
      "label": "礼藏原件"
    },
    {
      "name": "displayed",
      "label": "仪典借出"
    }
  ],
  "layout": "flip",
  "view": "grid",
  "actions": [
    {
      "name": "return_flag",
      "label": "签收借出旗面",
      "path": "/flag_archive/return-flag",
      "fields": [
        {
          "name": "flag",
          "label": "旗面号",
          "kind": "text",
          "initial": "FLAG-C3"
        },
        {
          "name": "receipt",
          "label": "归还凭据",
          "kind": "text",
          "initial": "RETURN-24"
        }
      ],
      "help": "在礼宾送回后复核纸本归还号。",
      "roles": [
        "reviewer"
      ],
      "success": "已写入"
    }
  ]
};

        export const {title} = page;
        export const key = "flag_archive";
        export async function render(root, role) {
          await workspace(root, role, page);

        }
