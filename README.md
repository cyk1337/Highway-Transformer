# Highway Transformer: Self-Gating Enhanced Self-Attentive Networks
[![ACL2020](https://img.shields.io/badge/Proceedings-ACL2020-red)](https://acl2020.org/) [![Highway Transformer](https://img.shields.io/badge/Transformers-Gating%20Transformer-orange)](https://www.aclweb.org/anthology/2020.acl-main.616.pdf) [![GitHub](https://img.shields.io/github/license/cyk1337/Highway-Transformer)](https://www.apache.org/licenses/LICENSE-2.0) 

This repo is the demo code of Transformer-XL using **Self-Dependency Unit**. This work is closedly related to Gating-enhanced Transformer variants, such as [Google's Switch Transformers](https://github.com/tensorflow/mesh/blob/master/mesh_tensorflow/transformer/moe.py).

Yekun Chai *et. al.*, [Highway Transformer: Self-Gating Enhanced Self-Attentive Networks](https://arxiv.org/abs/2004.08178) (ACL 2020)

## Requirements

- PyTorch >= 1.1.0
- TensorboardX >= 1.8
- Tensorboard >= 1.14
-  **4 GPUs** of each **8GB** memory for running 12 layer Transformer-XL

## Data download

`bash getdata.sh`

## Run 6-layer Transformer-XL
```bash
cd pytorch/xl_L6_scripts && bash <script-name>.sh train --work_dir "PATH_TO_WORK_DIR"
```

## Visualizing Your Result
```bash
cd XL-L6-results && tensorboard --logdir=.
```

## Results

- Line plots of different model settings, where the *topmost line (in red)* is the baseline model (i.e., original Transformer-XL). 
- After adding Self-Dependency Unit (see bottom two curves), it is clear that Highway Transformer **speeds up the convergence process** during training and evaluation.

training bpc    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        |  training loss&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
:-------------------------:|:-------------------------:
![alt-Training-1](fig/train_bpc.svg)  |  ![Training loss](fig/train_loss.svg)

 

 eval bpc  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;    |  eval loss &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
:-------------------------:|:-------------------------:
![eval BPC](fig/eval_bpc.svg)  |  ![eval BPC](fig/eval_loss.svg)



# Citation
For attribution in academic contexts, please cite this work as:
```
@inproceedings{chai-etal-2020-highway,
    title = "Highway Transformer: Self-Gating Enhanced Self-Attentive Networks",
    author = "Chai, Yekun  and
      Jin, Shuo  and
      Hou, Xinwen",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.616",
    pages = "6887--6900"
}
```
