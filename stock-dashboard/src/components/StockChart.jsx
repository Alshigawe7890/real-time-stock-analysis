import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

const StockChart = ({ data, symbol }) => {
  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>مخطط الأسعار - {symbol}</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis 
              dataKey="time" 
              tick={{ fontSize: 12 }}
            />
            <YAxis 
              tick={{ fontSize: 12 }}
              domain={['dataMin - 1', 'dataMax + 1']}
            />
            <Tooltip 
              labelFormatter={(value) => `الوقت: ${value}`}
              formatter={(value, name) => [`$${value?.toFixed(2)}`, 'السعر']}
            />
            <Line 
              type="monotone" 
              dataKey="price" 
              stroke="#2563eb" 
              strokeWidth={2}
              dot={false}
            />
          </LineChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  )
}

export default StockChart
