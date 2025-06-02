import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select";

export default function PriorAuthTool() {
  const [drugName, setDrugName] = useState("");
  const [plan, setPlan] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = () => {
    // Simulated response logic
    if (drugName.toLowerCase() === "ozempic" && plan === "md_medicaid") {
      setResult({
        paRequired: true,
        notes: "Step therapy required. Must try metformin first.",
        formLink: "https://example.com/md_form.pdf",
        alternatives: ["Metformin", "Rybelsus"]
      });
    } else {
      setResult({
        paRequired: false,
        notes: "No prior authorization required.",
        alternatives: []
      });
    }
  };

  return (
    <div className="max-w-xl mx-auto mt-10 space-y-6">
      <Card>
        <CardContent className="space-y-4 p-4">
          <h2 className="text-xl font-semibold">Prior Authorization Checker</h2>

          <Input
            placeholder="Enter drug name (e.g., Ozempic)"
            value={drugName}
            onChange={(e) => setDrugName(e.target.value)}
          />

          <Select onValueChange={(val) => setPlan(val)}>
            <SelectTrigger>
              <SelectValue placeholder="Select Insurance Plan" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="md_medicaid">Maryland Medicaid</SelectItem>
              <SelectItem value="dc_medicaid">DC Medicaid</SelectItem>
              <SelectItem value="ca_medicaid">California Medicaid</SelectItem>
            </SelectContent>
          </Select>

          <Button onClick={handleSubmit}>Check PA Status</Button>

          {result && (
            <div className="mt-6 space-y-2">
              <p className="font-medium">
                PA Required: {result.paRequired ? "Yes" : "No"}
              </p>
              <p>{result.notes}</p>
              {result.paRequired && result.formLink && (
                <a
                  href={result.formLink}
                  className="text-blue-600 underline"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Download PA Form
                </a>
              )}
              {result.alternatives.length > 0 && (
                <p>
                  <span className="font-medium">Covered Alternatives:</span> {result.alternatives.join(", ")}
                </p>
              )}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
