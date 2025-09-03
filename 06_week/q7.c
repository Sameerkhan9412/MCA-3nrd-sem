#include <stdio.h>

int main() {
    unsigned int ip1, ip2, ip3, ip4;
    unsigned int mask1, mask2, mask3, mask4;

    printf("Enter IPv4 address (e.g. 192.168.1.10): ");
    scanf("%u.%u.%u.%u", &ip1, &ip2, &ip3, &ip4);

    printf("Enter subnet mask (e.g. 255.255.255.0): ");
    scanf("%u.%u.%u.%u", &mask1, &mask2, &mask3, &mask4);

    // Calculate network address
    unsigned int net1 = ip1 & mask1;
    unsigned int net2 = ip2 & mask2;
    unsigned int net3 = ip3 & mask3;
    unsigned int net4 = ip4 & mask4;

    // Calculate broadcast address
    unsigned int bc1 = net1 | (~mask1 & 0xFF);
    unsigned int bc2 = net2 | (~mask2 & 0xFF);
    unsigned int bc3 = net3 | (~mask3 & 0xFF);
    unsigned int bc4 = net4 | (~mask4 & 0xFF);

    printf("\nNetwork ID: %u.%u.%u.%u\n", net1, net2, net3, net4);
    printf("Broadcast Address: %u.%u.%u.%u\n", bc1, bc2, bc3, bc4);

    // First and last host
    printf("First Host: %u.%u.%u.%u\n", net1, net2, net3, net4 + 1);
    printf("Last Host: %u.%u.%u.%u\n", bc1, bc2, bc3, bc4 - 1);                   

    // Calculate CIDR by counting bits in mask (simple version)
    int cidr = 0;
    unsigned int masks[4] = {mask1, mask2, mask3, mask4};
    int i;
	for(i=0;i<4;i++){
        unsigned int m = masks[i];
        int j;
        for (j = 0; j < 8; j++) {
            if ((m & (1 << (7 - j))) != 0) cidr++;
        }
    }
    printf("CIDR Notation: /%d\n", cidr);

    // Number of hosts
    unsigned int hosts = (1 << (32 - cidr)) - 2;
    if (hosts < 0) hosts = 0;
    printf("Number of valid hosts: %u\n", hosts);

    // Determine IP class based on first octet
    char ipclass;
    if (ip1 <= 127) ipclass = 'A';
    else if (ip1 <= 191) ipclass = 'B';
    else if (ip1 <= 223) ipclass = 'C';
    else if (ip1 <= 239) ipclass = 'D';
    else ipclass = 'E';

    printf("IP Address Class: %c\n", ipclass);

    return 0;
}

