module demo (
    out     ,  // Output of the counterq
    enable  ,  // enable for counter
    clk     ,  // clock Input
    reset      // reset Input
);

// Ports
output [7:0] out;
input enable, clk, reset;

// Internal Variables
reg [7:0] out;
// Generate Warning
parameter TEST = 4294967295;

always @(posedge clk)
if (rest) begin
    out <= 8'b0;
end else if (enable) begin
    out <= out+1;
end else begin
    out <= out;
end

endmodule
