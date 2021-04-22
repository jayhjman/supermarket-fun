apiVersion = "/v1.0"
genderInvoiceURL = apiVersion + "/genderinvoices"
customerTypeTotalURL= apiVersion + "/customertypetotal"
function loadData() {
  
  d3.json(genderInvoiceURL).then((pieData) => {
    console.log("gender invoices:");
    console.log(pieData);
    drawGenderPie(pieData["gender"], pieData["total"]);
  });

  d3.json(customerTypeTotalURL).then((pieData) => {
    console.log("gender invoices:");
    console.log(pieData);
    drawCustomerTypePie(pieData["customer_type"], pieData["total"]);
  });

}

function drawGenderPie(gender, total) {

  var trace = {
    values: total,
    labels: gender,
    pull: gender.map((x) => 0.05),
    type: "pie",
    rotation: 45,
    marker: {
        colors: ["red", "blue"],
    },
  } 

  var data = [trace];

  var layout = {
    height: 500,
    width: 500,
    title: "Distribution Of Invoices By Gender",
  };

  Plotly.newPlot("genderPie", data, layout);
}

function drawCustomerTypePie(customerType, total) {

  var trace = {
    values: total,
    labels: customerType,
    pull: customerType.map((x) => 0.05),
    type: "pie",
    rotation: 45,
  } 

  var data = [trace];

  var layout = {
    height: 500,
    width: 500,
    title: "Customer Type and Gender by Purchase Total",
  };

  Plotly.newPlot("customerTypePie", data, layout);
}
loadData();