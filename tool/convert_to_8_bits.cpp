#include <iostream>
#include <opencv2/opencv.hpp>
#include <string>
#include <stdio.h>
using namespace std;
using namespace cv;
int main(void){
    char buff1[100];
    char buff2[100];
    for(int i=1;i<901;i++){
        sprintf(buff1,"/home/cheng/ZED_lab/20220217/label_data/instance_segmentationt_data/SegmentationObjectPNG/left026092.png",i);
        sprintf(buff2,"/home/cheng/ZED_lab/20220217/label_data/instance_segmentationt_data/8_bits_SegmentationObjectPNG/left026092.png",i);
        //sprintf(buff1,"/media/lj/FA68-10A6/test_drug/disp/disp_%d.png",i);
        //sprintf(buff2,"/media/lj/FA68-10A6/test_drug/disp_8/disp_%d.png",i);
        Mat src;
        //Mat dst;
        src=imread(buff1,CV_LOAD_IMAGE_UNCHANGED);
        Mat ff=Mat::zeros(src.rows,src.cols,CV_8UC1);
        for(int k=0;k<src.rows;k++){
            for(int kk=0;kk<src.cols;kk++){
                int n=src.at<ushort>(k,kk);
                ff.at<uchar>(k,kk)=n;
            }
        }
        //src.copyTo(dst);
        //imshow("haha",ff*100);
        //waitKey(0);
        imwrite(buff2,ff);
    }
    return 0;
}
