# Copper-Heap-Leaching
This program models the heap leaching of copper from low-grade ores with a sulphuric acid lixiviant using the Avrami kinetic equation. The user inputs a total ore mass, ore grade, and the market price of copper in $/lb, then selects a preset heap height. The program uses this data to calculate OPEX (operating expenditures in $/day) and runs an economic analysis over the course of a full year. Finally, it generates a graph of time (days) vs total profit (millions of $) and total extracted copper (thousands of tons). The optimal day to shutoff the pumps (no more profit can be generated) is both printed and marked on the graph.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Citation**
The program utilizes Equation 1 and Table 1 from the following entry in the Minerals Engineering Journal for constant values and operational parameters:
Padilla, Gonzalo A., et al. “On the optimization of heap leaching.” Minerals Engineering, vol. 21, no. 9, 2008, pp. 673-678. ScienceDirect, https://www.sciencedirect.com/science/article/pii/S0892687508000046.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Installation & Usage 
git clone https://github.com/drp-u/Copper-Heap_Leaching
cd Copper-Heap_Leaching
pip install -r requirements.txt
python Cu_Heap_Leach.py
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SAMPLE:
<img width="1631" height="1233" alt="Screenshot 2026-06-02 144156" src="https://github.com/user-attachments/assets/de61b6a0-0d9b-4e3a-8924-e07ddac4b93a" />
