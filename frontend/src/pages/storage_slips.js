        import {workspace} from '../workspace.js';
        import {el} from '../dom.js';

        const page = {
  "title": "替班保管移交",
  "module": "礼具归档移交",
  "caption": "礼具归档移交",
  "detail": "归档动作同时核对旗面身份和借出状态。礼藏原件只允许原位特别保管。",
  "path": "/storage_slips",
  "columns": [
    {
      "name": "code",
      "label": "编号"
    },
    {
      "name": "guide",
      "label": "代表样凭据"
    },
    {
      "name": "flag",
      "label": "旗面"
    },
    {
      "name": "action",
      "label": "归档动作"
    },
    {
      "name": "locker",
      "label": "保管柜"
    },
    {
      "name": "witness",
      "label": "替班双签"
    }
  ],
  "layout": "flip",
  "view": "stack",
  "actions": [
    {
      "name": "handoff_flag",
      "label": "登记保管交接",
      "path": "/storage_slips/handoff-flag",
      "fields": [
        {
          "name": "code",
          "label": "移交号",
          "kind": "text",
          "initial": "STORE-24"
        },
        {
          "name": "guide",
          "label": "参考号",
          "kind": "text",
          "initial": "REFERENCE-24"
        },
        {
          "name": "action",
          "label": "动作",
          "kind": "text",
          "initial": "平放复核"
        },
        {
          "name": "locker",
          "label": "保管柜",
          "kind": "text",
          "initial": "A-11"
        },
        {
          "name": "witness",
          "label": "两位替班保管员",
          "kind": "text",
          "initial": "刘敏/陈明"
        }
      ],
      "help": "替班人员签认保管柜和动作。",
      "roles": [
        "reviewer"
      ],
      "success": "已写入"
    }
  ]
};

        export const {title} = page;
        export const key = "storage_slips";
        export async function render(root, role) {
          await workspace(root, role, page);

        }
