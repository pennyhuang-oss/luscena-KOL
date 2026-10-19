"""Turn the raw Metricool rows in data/raw_latest.json into data/stats.json for the dashboard.

Raw rows come from getAnalyticsDataByMetrics with metrics
THEV01 (Threads followers, LAST), THEV06 (Threads post views, SUM), THEV07 (Threads likes, SUM),
IGEV01 (IG followers, LAST), IGEV05 (IG views, SUM), IGEV13 (IG post likes, SUM), IGEV27 (IG reel likes, SUM).
"""
import json
import pathlib

HERE = pathlib.Path(__file__).parent
ACCOUNTS = [
    ("wendy", "Wendy Yeo", "冷艷女上司", "wendyyeo19980214"),
    ("kanon", "小森花音 Kanon", "地雷系萌妹", "kanon20060401"),
    ("vicky", "Vicky Lin", "陽光體育系辣妹", "vicky20010721"),
    ("nanami", "黃芷柔 Nanami", "成熟溫柔少婦", "nanami19990520"),
]


def num(v):
    return float(v) if v not in (None, "") else None


def main():
    raw = json.loads((HERE / "data" / "raw_latest.json").read_text(encoding="utf-8"))
    idx = {m: i for i, m in enumerate(raw["metrics"])}
    out = {"updatedAt": raw["fetchedAt"], "from": raw["from"], "to": raw["to"], "accounts": []}
    for key, name, role, handle in ACCOUNTS:
        rows = sorted(raw["brands"].get(key, []), key=lambda r: r[idx["date"]])
        daily, last = [], {"THEV01": None, "IGEV01": None}
        tot = {"thViews": 0, "thLikes": 0, "igViews": 0, "igLikes": 0}
        for r in rows:
            d = r[idx["date"]]
            day = {
                "date": f"{d[:4]}-{d[4:6]}-{d[6:]}",
                "thViews": num(r[idx["THEV06"]]) or 0,
                "thLikes": num(r[idx["THEV07"]]) or 0,
                "igViews": num(r[idx["IGEV05"]]) or 0,
                "igLikes": (num(r[idx["IGEV13"]]) or 0) + (num(r[idx["IGEV27"]]) or 0),
            }
            for k in tot:
                tot[k] += day[k]
            for k in last:
                if num(r[idx[k]]) is not None:
                    last[k] = num(r[idx[k]])
            daily.append(day)
        out["accounts"].append({
            "key": key, "name": name, "role": role, "handle": handle,
            "threads": {"followers": int(last["THEV01"] or 0), "views": int(tot["thViews"]), "likes": int(tot["thLikes"])},
            "instagram": {"followers": int(last["IGEV01"] or 0), "views": int(tot["igViews"]), "likes": int(tot["igLikes"])},
            "daily": daily,
        })
    (HERE / "data" / "stats.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([{a["key"]: [a["threads"], a["instagram"]]} for a in out["accounts"]], ensure_ascii=False))


if __name__ == "__main__":
    main()
