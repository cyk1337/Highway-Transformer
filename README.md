# Highway Transformer: Self-Gating Enhanced Self-Attentive Networks
This is a demo source code of SDU enhanced Transformer-XL in PyTorch, see the original paper for more details.

Yekun Chai *et. al.*, [Highway Transformer: Self-Gating Enhanced Self-Attentive Networks](https://ychai.uk/papers/ACL/SDU.pdf) (ACL 2020)

## Requirements

- Pytorch >= 1.1.0
- TensorboardX >= 1.8
- Tensorboard >= 1.14
-  **4 GPUs** of each **8GB** memory for running 12 layer Transformer-XL

## Data download

`bash getdata.sh`

## Run the demo with 6-layer Transformer-XL
```bash
cd pytorch/xl_L6_scripts && bash <script-name>.sh train --work_dir "PATH_TO_WORK_DIR"
```
## Results
The training bpc of different model settings, where the topmost line (in red) is the original Transformer-XL (baselines).
![Training BPC](pngs/train_bpc.svg)

Line plot of training loss.
![Training loss](pngs/train_loss.svg)

Line plot of evaluation bpc:
![eval BPC](pngs/eval_bpc.svg)

Line plot of evaluation loss:
![eval BPC](pngs/eval_loss.svg)

# Cite
```
@inproceedings{chai2020highway,
  title={Semi-Supervised Classification with Graph Convolutional Networks},
  author={Yekun, Chai and Shuo, Jin and Xinwen, Hou},
  booktitle={Proceedings of the 2020 Annual Conference of the Association for Computational Linguistics, {ACL} 2020, Seattle, Washington, United States, July 5–July 10, 2020},
  year={2020}
}
```