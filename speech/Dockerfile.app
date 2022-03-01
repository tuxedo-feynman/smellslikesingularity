FROM fastdotai/fastai:2020-10-02

RUN useradd fastai-user 

RUN apt-get update 

RUN apt-get -y install graphviz \
   libwebp-dev \
   curl \
   htop \
   ffmpeg

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && apt-get -y install nodejs
RUN node -v

## VIM #######################################################
## # install dependencies
RUN apt-get -y install libncurses5-dev libncursesw5-dev
RUN apt -y install git
RUN apt -y install make
RUN apt -y install build-essential

## # get source code / checkout version
RUN git clone https://github.com/vim/vim.git
RUN cd vim && git checkout tags/v8.2.4460

## # build vim
RUN pip install pynvim
RUN cd vim/src && make install
##############################################################

# Speech Project Dependencies ###########
RUN apt-get -y install libsndfile1
########################################

#RUN pip uninstall -y pillow
#RUN pip install pillow 
#    
#RUN pip install kaggle \
#    dtreeviz \
#    treeinterpreter
#
#RUN pip install waterfallcharts

WORKDIR /home/

WORKDIR /home/fastai-user/

RUN chown -R fastai-user:fastai-user /home/fastai-user
 
USER fastai-user

ENV HOME "/home/fastai-user"
