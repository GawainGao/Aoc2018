class day11_1 {

	    public static void main(String[] args){
			        int[][] fuelCell = new int[300][300];
					        int[][] sum = new int[298][298];
							        int serialNumber = 9445;

									        for (int i = 0; i< fuelCell.length; i++){
												            for (int j = 0; j< fuelCell[0].length; j ++){
																                fuelCell[i][j] = ((i + 10) * j + serialNumber) * (i + 10) / 100 % 10 - 5;
																				            }
															        }
											        int max = 0;
													        int max_x = 0;
															        int max_y = 0;
																	        for (int i = 0; i< sum.length; i++){
																				            for (int j = 0; j< sum[0].length; j ++){
																								                for (int k = 0; k < 3; k ++){
																													                    for (int t = 0; t < 3; t++){
																																			                        sum[i][j] += fuelCell[i+k][j+t];
																																									                    }
																																		                }
																												                max = (max > sum[i][j])? max:sum[i][j];
																																                if (max == sum[i][j]){
																																					                    max_x =i;
																																										                    max_y =j;
																																															                }
																																				            }
																							        }
																			        System.out.println(max + " " + max_x + " " + max_y);





																					    }


}

