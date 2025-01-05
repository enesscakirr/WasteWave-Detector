from ultralytics import YOLO

# Modeli yükle
model = YOLO('runs/train/exp4/weights/best.pt')


video_path = "../Videos/test27.mp4"

# Modeli video üzerinde çalıştır ve sonucu kaydet
model.predict(
    source=video_path,  # Test edilecek video
    save=False,         # Tahmin sonuçlarını kaydet
    save_txt=False,     # Tahmin sonuçlarını .txt olarak kaydet (opsiyonel)
    save_conf=True,     # Tahmin sonuçlarına güven skoru ekle (opsiyonel)
    conf=0.25,          # Minimum güven skoru (varsayılan: 0.25)
    show=True           # Sonuçları gerçek zamanlı göster (opsiyonel)
)