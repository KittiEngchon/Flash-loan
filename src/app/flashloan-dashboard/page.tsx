import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { CheckCircle, AlertCircle, Loader } from "lucide-react";
import { useEffect, useState } from "react";

const mockStrategies = [
  {
    name: "Arbitrage ETH/USDT",
    status: "running",
    lastProfit: "$12.34",
    txHash: "0x1234...abcd"
  },
  {
    name: "Sandwich Bot",
    status: "idle",
    lastProfit: "$0.00",
    txHash: "-"
  },
  {
    name: "Liquidation Sniper",
    status: "error",
    lastProfit: "$7.89",
    txHash: "0xdead...beef"
  }
];

export default function FlashloanDashboard() {
  const [strategies, setStrategies] = useState([]);

  useEffect(() => {
    // ในระบบจริงให้ fetch จาก backend API
    setTimeout(() => setStrategies(mockStrategies), 1000);
  }, []);

  const getStatusBadge = (status) => {
    switch (status) {
      case "running":
        return <Badge className="bg-green-500"><CheckCircle className="w-4 h-4 mr-1" /> Running</Badge>;
      case "idle":
        return <Badge className="bg-gray-400">Idle</Badge>;
      case "error":
        return <Badge className="bg-red-500"><AlertCircle className="w-4 h-4 mr-1" /> Error</Badge>;
      default:
        return <Badge>Unknown</Badge>;
    }
  };

  return (
    <div className="p-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {strategies.length === 0 ? (
        <div className="col-span-full flex justify-center items-center text-gray-500">
          <Loader className="animate-spin w-6 h-6 mr-2" /> Loading strategies...
        </div>
      ) : (
        strategies.map((s, i) => (
          <Card key={i} className="rounded-2xl shadow-md">
            <CardContent className="p-4 space-y-2">
              <div className="text-xl font-semibold">{s.name}</div>
              <div>{getStatusBadge(s.status)}</div>
              <div className="text-sm text-gray-500">Last Profit: {s.lastProfit}</div>
              <div className="text-xs text-gray-400">TX: {s.txHash}</div>
              <Button variant="outline" className="mt-2">View Details</Button>
            </CardContent>
          </Card>
        ))
      )}
    </div>
  );
}
