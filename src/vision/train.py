import torch
from ultralytics import YOLO


def train_yolo_model():
    """训练YOLO模型"""

    # 检查设备
    if torch.backends.mps.is_available():
        device = "mps"
        print("使用 macOS MPS 后端进行训练")
    else:
        device = "cpu"
        print("MPS 不可用，使用 CPU 进行训练")

    # 加载模型
    print("加载YOLO模型...")
    model = YOLO("yolo11m.pt")

    # 训练参数
    train_args = {
        "project": "data/yolo",
        "data": "data/yolo/dataset/dataset.yaml",
        "epochs": 100,
        "batch": 32,
        "patience": 5,
        "imgsz": 640,
        "device": device,
        "workers": 0 if device == "mps" else 4,  # MPS下workers设为0
        "save": True,
        "exist_ok": True,
        "verbose": True,
    }

    # 开始训练
    print("开始训练模型...")
    results = model.train(**train_args)

    print("训练完成!")
    print("最佳模型保存在: data/yolo/train/weights/best.pt")

    return model, results


if __name__ == "__main__":
    train_yolo_model()
