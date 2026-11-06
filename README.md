# Systems Architecture & Quantitative Corporate Tax Research Index (2026)

An open technical reference index covering Linux Kernel internals (`sk_buff`, `SLUB`, `RCU`, `NVMe-oF io_uring_cmd`), High-Frequency Interconnects (`PCIe 6.0 / CXL 3.1`, `SR-IOV / IOMMU`, `RoCEv2`), and U.S. Corporate M&A Tax Mechanics (`IRC § 382`, `§ 338(h)(10)`, `§ 368 / § 355`, `§ 704(b)/(c)`, `§ 409A / § 280G`).

---

## 1. Linux Kernel, Storage & Network Datapath Architecture

| Subsystem / Protocol | Core Kernel Structs & Hardware Mechanisms | Full Technical Paper |
| :--- | :--- | :--- |
| **NVMe over Fabrics (NVMe-oF) & `io_uring` Passthru** | `IORING_OP_URING_CMD`, `/dev/ngXnY` VFS bypass, `NVMe/RDMA` vs. `NVMe/TCP` capsules, and PCIe `p2pdma` zero-copy DMA | [Read Full Analysis](https://trendspike.online/post.php?slug=nvme-over-fabrics-nvme-of-rdma-tcp-io-uring-cmd-passthru-pcie-p2pdma-architecture) |
| **Linux Kernel Memory Management (`SLUB` & `THP`)** | Lockless `kmem_cache_cpu` double-word `cmpxchg_double` fastpaths, 5-level `PGD/P4D/PUD/PMD/PTE` walks, and `struct folio` THP | [Read Full Analysis](https://trendspike.online/post.php?slug=linux-kernel-memory-management-slub-allocator-page-tables-transparent-huge-pages-tlb) |
| **Linux Kernel `RCU` (Read-Copy-Update) Concurrency** | Lockless `rcu_read_lock()` critical sections, hierarchical `struct rcu_node` grace-period trees, and `rcu_segcblist` offloading | [Read Full Analysis](https://trendspike.online/post.php?slug=linux-kernel-rcu-read-copy-update-synchronization-tree-grace-periods-lockless-concurrency) |
| **Hardware I/O Virtualization (`SR-IOV` & `IOMMU`)** | PCIe SR-IOV `PF/VF` BAR routing, two-stage nested IOMMU page tables (`GIOVA -> GPA -> HPA`), and `ATS/PRI` Device-IOTLB | [Read Full Analysis](https://trendspike.online/post.php?slug=hardware-io-virtualization-iommu-dma-remapping-pcie-sr-iov-ats-pasid-architecture) |
| **Linux Socket Buffer (`struct sk_buff`) & `NAPI`** | Ring-buffer DMA descriptors, `skb_shared_info` page frags, `NET_RX_SOFTIRQ` NAPI polling, and `GRO/TSO` coalescing | [Read Full Analysis](https://trendspike.online/post.php?slug=linux-socket-buffer-sk-buff-architecture-driver-queues-napi-polling) |
| **PCIe 6.0 & CXL 3.1 Memory Pooling** | 64 GT/s PAM4 signaling, 256-byte FLIT framing, forward error correction (FEC), and `CXL.mem` hardware coherency | [Read Full Analysis](https://trendspike.online/post.php?slug=pcie-6-0-cxl-3-1-architecture-pam4-signaling-flit-mode-memory-pooling) |
| **Lossless Ethernet AI Fabrics (`RoCEv2` & `UET`)** | Priority Flow Control (`PFC`) deadlock prevention, `ECN/DCQCN` rate control, and Ultra Ethernet Transport packet spraying | [Read Full Analysis](https://trendspike.online/post.php?slug=lossless-ethernet-ai-clusters-rocev2-pfc-ecn-dcqcn-ultra-ethernet-transport) |
| **IEEE 1588v2 PTP & TrueTime Synchronization** | Hardware PHY/MAC timestamping, Boundary/Transparent Clocks, and distributed commit-wait uncertainty bounds ($2\epsilon$) | [Read Full Analysis](https://trendspike.online/post.php?slug=ieee-1588v2-ptp-precision-time-protocol-hardware-timestamping-truetime-sync) |

---

## 2. U.S. Corporate M&A, International & Partnership Tax Modeling

| Internal Revenue Code Regime | Statutory Formulas & Treasury Regulations | Full Technical Analysis |
| :--- | :--- | :--- |
| **Subchapter K Partnership Tax (`IRC § 704(b)` & `§ 704(c)`)** | Substantial Economic Effect (`Treas. Reg. § 1.704-1(b)(2)`), Traditional/Curative/Remedial `§ 704(c)` allocations, and `§ 752` debt tiers | [Read Full Analysis](https://trendspike.online/post.php?slug=irc-section-704b-substantial-economic-effect-section-704c-built-in-gain-partnership-tax) |
| **Tax-Free Corporate Reorganizations (`IRC § 368` & `§ 355`)** | Forward/Reverse Triangular Mergers (`§ 368(a)(2)(D)/(E)`), `COI/COBE` safe harbors, `§ 356` boot-within-gain, and `§ 355(e)` Morris Trust | [Read Full Analysis](https://trendspike.online/post.php?slug=irc-section-368-tax-free-corporate-reorganizations-section-355-spin-offs-boot-tax) |
| **Deemed Asset Acquisitions (`IRC § 338(h)(10)` & `§ 336(e)`)** | Iterative `ADSP` and `AGUB` gross-up equations, `IRC § 1060` 7-class purchase price waterfall, and 15-year `§ 197` amortization shields | [Read Full Analysis](https://trendspike.online/post.php?slug=irc-section-338-h-10-deemed-asset-acquisition-adsp-agub-section-197-amortization) |
| **Net Operating Loss (`NOL`) Limitations (`IRC § 382`)** | 50-percentage-point 3-year ownership change testing, Long-Term Tax-Exempt Rate caps, and `Notice 2003-65` `NUBIG` / `338` vs. `1374` | [Read Full Analysis](https://trendspike.online/post.php?slug=irc-section-382-nol-ownership-change-limitation-nubig-corporate-tax) |
| **International Tax (`IRC § 951A GILTI` & `§ 250 FDII`)** | `QBAI` 10% deemed tangible return, `IRC § 960(d)` 80% foreign tax credit haircut, and the 18.9% GILTI High-Tax Exclusion | [Read Full Analysis](https://trendspike.online/post.php?slug=irc-section-951a-gilti-section-250-fdii-qbai-subpart-f-international-tax) |
| **Corporate Alternative Minimum Tax (`CAMT` 15% & `OECD Pillar Two`)** | `IRC § 55 / § 56A` Adjusted Financial Statement Income (`AFSI`), `QDMTT` safe harbours, and `IIR / UTPR` top-up tax mechanics | [Read Full Analysis](https://trendspike.online/post.php?slug=corporate-alternative-minimum-tax-camt-15-percent-afsi-rules-2026-guidance) |
