<!-- PROJECT LOGO -->
<p align="center">
  
  <h1 align="center">CLOTH4D: A Dataset for Clothed Human Reconstruction</h1>
  <p align="center">
    <a href="https://github.com/AemikaChow/"><strong>Xingxing Zou</strong></a>
    ·
    <a href="https://github.com/xthan"><strong>Xintong Han</strong></a>
    ·
    <a href="https://www.aidlab.hk/en/people-detail/prof-calvin-wong"><strong>Waikeung Wong</strong></a>
  </p>
  <h2 align="center">CVPR 2023</h2>
  <div align="center">
    <img src="./media/first_pages-to-jpg-0001.jpg" alt="Logo" width="100%">
  </div>


<br />
<br />

## Quick View

<div align="center">
    <img src="./media/quick.jpg" alt="Logo" width="100%">
</div>

## How to Use

- 【[**Obtain Subset of CLOTH4D**](https://polyuit-my.sharepoint.com/:f:/g/personal/xingxzou_polyu_edu_hk/EhYDkcEaAztBsDWLdzbTaj0BWu_p63T3IoIHXHhbH-caVA?e=9mnbfR)】 We prepare 30,000 meshes for direct usage. You can check the [samples](https://polyuit-my.sharepoint.com/:f:/g/personal/xingxzou_polyu_edu_hk/Ep6KnfQulLxLl74dI_qlbD4BQnzRAlhWgM1zvZQU00baRA?e=6NwdeC) before downloading the whole subset. The structure is similar to [Thuman2](https://github.com/ytrock/THuman2.0-Dataset), organized into three folders: scans, smplx (smplx in CLOTH4D refers to the naked model), and 8_views. Thus, you can directly train or test on any Thuman2 compatible repos. For example, using [ICON](https://github.com/YuliangXiu/ICON). 

- 【**Obtain the Source Files of Outfits and Fabric Prints and Materials**】 We also willing to share the source files of 3D outfits for community to create more 3D/4D clothed human data. All the outfits are created in professional 3D software in fashion with high quality. You can preview all ready-for-sharing outfits [here](https://polyuit-my.sharepoint.com/:f:/g/personal/xingxzou_polyu_edu_hk/Eiu94bo06i9LkVO2XHAdjZIBpMvoCWLRrZJdUiSkDyx4MA?e=0WWMu1). They are rich in prints, materials, details designs, and, most importantly, realistic (e.g., a clothed human in the real world is not water-tight). As reported in our paper, although current SOTAs achieved astonishing results, they still have space on CLOTH4D. If you want to access this part of the data, you could connect with our business manager [**Barry Tai**](https://www.aidlab.hk/en/people-detail/barry-tai-) via barrytai@aidlab.hk. You may need to sign an agreement with us before getting the data. We aim to share this for academic usage and push toward a more realistic and temporally coherent clothed human reconstruction.

- 【[**Data Generation Pipeline**](DataGenerationPipeline.md)】We provide instructions to create CLOTH4D-type data.

## Citation
```bib
@inproceedings{zou2023cloth4d,
  title={CLOTH4D: A Dataset for Clothed Human Reconstruction},
  author={Zou, Xingxing and Han, Xintong and Wong, Waikeung},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={12847--12857},
  year={2023}
}
```

<br>


<br>
