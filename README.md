# Play-With-MEE6

<img src="https://static.wikia.nocookie.net/discord/images/e/e6/Mee6.png/revision/latest?cb=20201028153812" width = "150" height = "150" alt="图片名称" align=center />

本專案可自動發訊息與 Discord 機器人 MEE6 遊玩<br>
目前功能有
1. 每日簽到
2. 工作
3. 骰子遊戲

## Setup
* `pip3 install -r requirements.txt` 安裝本專案所需的 package
* `.env` 檔中輸入相關資訊
  * `GAMBLE` 玩骰子時發送訊息的頻道 ID，多個頻道用逗號隔開
  * `WORK` 工作時發送訊息的頻道 ID，多個頻道用逗號隔開
  * `Daily` 每日簽到發送訊息的頻道 ID，多個頻道用逗號隔開
  * `NAME` Discord 使用者名稱
  * `TOKEN` 伺服器的貨幣，預設為:coin:
  * `PERSON_ID` Discord 使用者的 ID
  * `AUTHORIZATION` 授權碼，不可外流!!!<br>
    用瀏覽器開 discord，然後打開開發人員選項找到 network
    隨便發一條訊息後會看到 network 下面出現 messages
    在 messages 的 headers 中可以找到
* 頻道 ID 在要發訊息的頻道按右鍵有複製 ID 選項
* 使用者 ID 在伺服器右側找到自己的名字，按右鍵一樣可以複製
## 每日簽到
```python
python daily.py -t h:m:s
```
每天固定在 h 時 m 分 s 秒簽到
## 工作
```python
python work.py -d h
```
一小時工作一次，工作 h 小時
沒給 `-d` 參數預設為一直工作下去
## 骰子遊戲
```python
python dice.py -t 100 -b 20
```
玩 100 次骰子，每次下注 20
```python
python dice.py -t 100 -d 30
```
玩 100 次骰子，每次下注本金除以 30

`-t` 預設為 200<br>
`-b` 和 `-d` 只能擇一，都沒選則預設下注金額為本金除以 50<br>
每次遊玩後會將輸贏的次數存入 `result.txt` 中
## 其他
參數不懂可以輸入 `python 檔名.py -h` 查詢