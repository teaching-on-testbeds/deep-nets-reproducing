## Deep Neural Nets: 33 years ago and 33 years from now

_Fraida Fund_

---

**Attribution**: This sequence of notebooks is adapted from the ICLR 2022 blog post ["Deep Neural Nets: 33 years ago and 33 years from now"](https://iclr-blog-track.github.io/2022/03/26/lecun1989/)  by Andrej Karpathy, and the associated [Github repository](https://github.com/karpathy/lecun1989-repro). 

---


In this sequence of experiments, you will reproduce a result from machine learning from 1989 - a paper that is possibly the earliest real-world application of a neural network trained end-to-end with backpropagation. (In earlier neural networks, some weights were actually hand-tuned!) You'll go a few steps further, though - after reproducing the results of the original paper, you'll get to use some modern 'tricks' to try and improve the performance of the model without changing its underlying infrastructure (i.e. no change in inference time!)

You can run this experiment on Google Colab: <a target="_blank" href="https://colab.research.google.com/github/teaching-on-testbeds/deep-nets-reproducing/blob/main/Deep_Neural_Nets_33_years_ago.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>



Or, you can use the Chameleon testbed: 
<a target="_blank" href="https://chameleoncloud.org/experiment/share/c0b5a325-b42c-4d44-bbb1-f2d9be7911d4">
  <img src='https://d31tc1b63hlzap.cloudfront.net/b0qmdz%2Fpreview%2F58757570%2Fmain_large.png' alt="Run on Chameleon"/>
</a> First, you'll run the `reserve.ipynb` notebook to bring up a resource on Chameleon and configure it with the software needed to run this experiment. At the end of this notebook, you'll set up an SSH tunnel between your local device and a Jupyter notebook server that you just created on your Chameleon resource. Then, you'll open the notebook server in your local browser and run the sequence of notebooks you see there.
