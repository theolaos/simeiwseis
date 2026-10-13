$$\text{Power In } (P_{\text{in}}) \approx \text{Power Out } (P_{\text{out}})$$
Brushless Fan needs $24V$ and Consumes $70mA$
$$P_{\text{fan}} = 24\text{V} \times 0.07\text{A} = 1.68\text{W}$$
Meaning that $P_{\text{fan}}$ Is the $\text{Power Out } (P_{\text{out}})$. But there are losses to temperature as efficiency of boosting is not $100\%$:

Lets assume that efficiency is at $\eta = 85\%$, $0.85$:

$$P_{\text{in}} = \frac{P_{\text{fan}}}{\eta}$$
We also know that the Voltage that the Raspberry Pi can give is at $3V$. So we can solve for the Amperage needed.

$$P_{\text{in}} =\frac{1.68\text{W}}{0.85} \approx 1.98\text{W} \ \ \ I_{\text{in}} = \frac{P_{\text{in}}}{V_{\text{in}}} = \frac{1.98\text{W}}{5\text{V}} \approx 0.395\text{A} \quad (395\text{mA})$$


## Raspberry Power Calc

- Power Supply is: $27W$

Consumption Numbers:
- Max Raspberry Pi consumption is: $9W$ to $10W$
- Cooler Chip fan: $0.5W$
- SSD Cooler Fan: $2W$
- 512GB Nvme on the HAT: $6.6W$
- 2TB disc: $8W$
- 512GB disc: $15W$ (P210 512gb, not usable with that consumption)
- 128GB disc: $5W$