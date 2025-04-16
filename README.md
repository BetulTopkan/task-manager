# Discord Görev Takip Botu

Bu proje, kullanıcıların Discord üzerinden görev eklemesine, silmesine, görüntülemesine ve tamamlandı olarak işaretlemesine olanak tanıyan basit bir görev yönetim botudur.

## 🚀 Özellikler

- **Görev ekleme:** Yeni görevler oluşturabilirsiniz.
- **Görev silme:** Mevcut görevleri silebilirsiniz.
- **Görev listesini görüntüleme:** Kayıtlı tüm görevleri listeleyebilirsiniz.
- **Görev tamamlama:** Tamamlanan görevleri işaretleyebilirsiniz.

## 🛠️ Kurulum

1. **Projeyi klonlayın:**

   ```bash
   git clone [https://github.com/betultopkan/task-managergit](https://github.com/betultopkan/task-manager.git)
   cd task-manager
   ```

2. **Gerekli paketleri yükleyin:**

   ```bash
   pip install -r requirements.txt

   ```

3. **`bot.py` dosyasındaki bot token'ınızı kendi Discord bot token’ınızla değiştirin:**

   ```python
   bot.run('YOUR_BOT_TOKEN')
   ```

## 🧪 Testler

Botun veritabanı işlemlerini test etmek için aşağıdaki komutu çalıştırabilirsiniz:

```bash
python run_tests.py


## 📋 Komutlar

| Komut                    | Açıklama                                                               |
| ----------------------   | -------------------------------------------------------                |
| `!add_task <açıklama>`   | Açıklaması olan bir görev ekler.                                       |
| `!delete_task <task_id>` | `<task_id>` tanımlayıcısına sahip görevi siler.                        |
| `!show_tasks`            | Tüm görevlerin bir listesini gösterir.                                 |
| `!complete_task <task_id>| `<task_id>` tanımlayıcısına sahip görevi tamamlandı olarak işaretler.  |

```
