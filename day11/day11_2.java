class day11_2 {

	    public static void main(String[] args){
			        int[][] sum = new int[301][301];
					        int serialNumber = 9445;

							        for (int i = 1; i< sum.length; i++){
										            for (int j = 1; j< sum.length; j ++){
														                int num = (((i+10) * j + serialNumber) * (i+10)) / 100 % 10 - 5;
																		                sum[i][j] = num + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1];
																						            }
													        }
									        int max = 0;
											        int max_x = 0;
													        int max_y = 0;
															        int max_size = 1;
																	        for (int s = 1; s< sum.length; s++){
																				            for (int i = s; i< sum.length; i++){
																								                for (int k = s; k< sum.length; k++){
																													                    int val = sum[i][k] - sum[i-s][k] - sum[i][k-s] + sum[i-s][k-s];
																																		                    max = (max > val)? max:val;
																																							                    if (max == val) {
																																													                        max_x = i - s + 1;
																																																			                        max_y = k - s + 1;
																																																									                        max_size = s;
																																																															                    }
																																												                }
																												            }
																							        }
																			        System.out.println(max + " " + max_x + " " + max_y + " " + max_size);





																					    }


}

