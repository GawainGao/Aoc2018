import demo.DefaultXYDatasetDemo1;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.StandardChartTheme;
import org.jfree.chart.annotations.XYTextAnnotation;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.data.xy.DefaultXYDataset;
import org.jfree.ui.RefineryUtilities;

import java.awt.*;
import java.io.*;
import java.util.*;
import java.util.List;

class PointsT {
    int x;
    int y;
    int speed_x;
    int speed_y;
    PointsT(String in){
        String[] left = in.split(",");
        x = Integer.parseInt(left[0].substring(11)) * (int)Math.pow(-1,((left[0].charAt(10) == '-')?1:2));
        y = Integer.parseInt(left[1].substring(2, 7)) * (int)Math.pow(-1,((left[1].charAt(1) == '-')?1:2));
        speed_x = Integer.parseInt(left[1].substring(20)) * (int)Math.pow(-1,((left[1].charAt(19) == '-')?1:2));
        speed_y = Integer.parseInt(left[2].substring(2, 3)) * (int)Math.pow(-1,((left[2].charAt(1) == '-')?1:2));
        System.out.println(x + " " + y + " " + speed_x + " " + speed_y);
    }
}

class ScatterPlot {
    static void data(String title, int[] a, int[] b) {
        DefaultXYDataset xydataset = new DefaultXYDataset();

        double[][] data = new double[2][a.length];
        for (int i = 0; i < a.length; i++) {
            data[0][i] = a[i];
            data[1][i] = b[i];
        }
        xydataset.addSeries("Result", data);
        final JFreeChart chart = ChartFactory.createScatterPlot("", "", "", xydataset, PlotOrientation.VERTICAL, false, false, false);
        ChartFrame frame = new ChartFrame(title, chart);
        frame.pack();
        RefineryUtilities.centerFrameOnScreen(frame);
        frame.setVisible(true);
    }
}

public class Main {

    public static void main(String[] args) throws Exception {
        File file = new File("/Users/gaoyuan/Developer/Java/aoc2018/GaoYuan/day10.txt");
        Scanner input = new Scanner(file);
        List<String> inputList = new ArrayList<>();
        while (input.hasNextLine()) {
            inputList.add(input.nextLine());
        }
        List<PointsT> pointsTList = new ArrayList<>();
        for (String in : inputList) {
            PointsT point = new PointsT(in);
            pointsTList.add(point);
        }
        int max_x = pointsTList.get(0).x;
        int min_x = pointsTList.get(0).x;
        int max_y = pointsTList.get(0).y;
        int min_y = pointsTList.get(0).y;
        for (PointsT point: pointsTList){
            max_x = (point.x > max_x)?point.x:max_x;
            min_x = (point.x < min_x)?point.x:min_x;
            max_y = (point.y > max_y)?point.y:max_y;
            min_y = (point.y < min_y)?point.y:min_y;
        }
        System.out.println("Max_x:" + max_x + "Min_x:" + min_x + "Max_y:" + max_y + "Min_y" + min_y);
        int[] x_series = new int[inputList.size()];
        int[] y_series = new int[inputList.size()];

        for (int t = 10350; t < 10370; t++){
			for (int count = 0; count < inputList.size(); count++){
                x_series[count] = pointsTList.get(count).x + t * pointsTList.get(count).speed_x;
                y_series[count] = pointsTList.get(count).y + t * pointsTList.get(count).speed_y;
                System.out.println(x_series + " " + y_series);
            }
            ScatterPlot.data("Result",x_series,y_series);
        }
    }
}










