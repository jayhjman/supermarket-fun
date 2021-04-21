apiVersion = "/v1.0"
genderInvoiceURL = apiVersion + "/genderinvoices"

function loadData() {
  d3.json(genderInvoiceURL).then((pieData) => {
    console.log("gender invoices:");
    console.log(pieData);
    drawPie();
  });
}

function drawPie() {
  var data = [
    {
      values: [19, 26, 55],
      labels: ["Residential", "Non-Residential", "Utility"],
      type: "pie",
    },
  ];

  var layout = {
    height: 400,
    width: 500,
  };

  Plotly.newPlot("genderPie", data, layout);
}

loadData();