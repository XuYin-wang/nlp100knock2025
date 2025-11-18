import os
import subprocess

# 输出目录
out_dir = "out"
os.makedirs(out_dir, exist_ok=True)

# 获取所有 3-*.py 文件
for filename in sorted(os.listdir(".")):
    if filename.startswith("3-") and filename.endswith(".py"):
        out_path = os.path.join(out_dir, filename.replace(".py", ".txt"))
        print(f"Running {filename} ...")
        result = subprocess.run(["python3", filename], capture_output=True, text=True)
        with open(out_path, "w") as f:
            f.write(result.stdout)
print("✅ 所有结果已保存到 out/ 文件夹中。")