        import {workspace} from '../workspace.js';
        import {el} from '../dom.js';

        const page = {
  "title": "模型试算工作台",
  "module": "旗面折态模型",
  "caption": "折态模型版本",
  "detail": "新版模型先在工作台试算再上线：发起时定下拟合用的签认样条，与在用版拿同一批留样逐条比代表样，复核批准后整版切换。",
  "path": "/model_trials",
  "columns": [
    {
      "name": "code",
      "label": "版本号"
    },
    {
      "name": "status",
      "label": "状态"
    },
    {
      "name": "baseline",
      "label": "对照版"
    },
    {
      "name": "fit",
      "label": "拟合样条"
    },
    {
      "name": "holdout",
      "label": "留样"
    },
    {
      "name": "token",
      "label": "计算号"
    },
    {
      "name": "report",
      "label": "比对报告"
    }
  ],
  "layout": "stack",
  "view": "table",
  "actions": [
    {
      "name": "launch_trial",
      "label": "发起试算",
      "path": "/model_trials/launch-trial",
      "fields": [
        {
          "name": "code",
          "label": "版本号",
          "kind": "text",
          "initial": "FM-1"
        },
        {
          "name": "holdout",
          "label": "留样编号（逗号分隔）",
          "kind": "text",
          "initial": "CK-00, CK-02, CK-04"
        }
      ],
      "help": "发起试算并定下拟合用的签认样条；留样所在旗面两版都不拿来拟合。",
      "roles": [
        "operator",
        "reviewer"
      ],
      "success": "已发起"
    },
    {
      "name": "resume_trial",
      "label": "续跑试算",
      "path": "/model_trials/resume-trial",
      "fields": [
        {
          "name": "code",
          "label": "版本号",
          "kind": "text",
          "initial": "FM-1"
        }
      ],
      "help": "试算中断后用原来的样条和留样续跑。",
      "roles": [
        "operator",
        "reviewer"
      ],
      "success": "已续跑"
    },
    {
      "name": "collect_trial",
      "label": "收取比对报告",
      "path": "/model_trials/collect-trial",
      "fields": [
        {
          "name": "code",
          "label": "版本号",
          "kind": "text",
          "initial": "FM-1"
        }
      ],
      "help": "试算计算完成后收取逐条比对报告，版本转入待批准。",
      "roles": [
        "operator",
        "reviewer"
      ],
      "success": "已收取"
    },
    {
      "name": "recompare_trial",
      "label": "重新比对",
      "path": "/model_trials/recompare-trial",
      "fields": [
        {
          "name": "code",
          "label": "版本号",
          "kind": "text",
          "initial": "FM-1"
        }
      ],
      "help": "对照版已被换下时，按当前在用版重新逐条比对。",
      "roles": [
        "operator",
        "reviewer"
      ],
      "success": "已重新比对"
    },
    {
      "name": "approve_trial",
      "label": "批准上线",
      "path": "/model_trials/approve-trial",
      "fields": [
        {
          "name": "code",
          "label": "版本号",
          "kind": "text",
          "initial": "FM-1"
        }
      ],
      "help": "复核员批准后整版一次性切换；新单立刻用新版查代表样，排队的还用受理时那版。",
      "roles": [
        "reviewer"
      ],
      "success": "已上线"
    }
  ]
};

        export const {title} = page;
        export const key = "model_trials";
        export async function render(root, role) {
          await workspace(root, role, page);

        }
