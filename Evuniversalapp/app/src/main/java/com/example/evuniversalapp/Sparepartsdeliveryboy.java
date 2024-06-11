package com.example.evuniversalapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONObject;

public class Sparepartsdeliveryboy extends AppCompatActivity implements JsonResponse {
    EditText e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12;
    Button b1;
    String fname,lname,address,place,latitude,pincode,phone,email,username,password,longitude;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sparepartsdeliveryboy);
        e1=(EditText) findViewById(R.id.fname);
        e2=(EditText) findViewById(R.id.lname);
        e3=(EditText) findViewById(R.id.place);
        e4=(EditText) findViewById(R.id.phone);

        e5=(EditText) findViewById(R.id.email);
        e6=(EditText) findViewById(R.id.uname);
        e7=(EditText) findViewById(R.id.password);


        b1=(Button) findViewById(R.id.dbregistration);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                fname=e1.getText().toString();
                lname=e2.getText().toString();
                place=e3.getText().toString();
                phone=e4.getText().toString();
                email=e5.getText().toString();
                username=e6.getText().toString();
                password=e7.getText().toString();


                JsonReq JR = new JsonReq();
                JR.json_response = (JsonResponse) Sparepartsdeliveryboy.this;
                String q = "/Sparepartsdeliveryboy?fname=" + fname + "&lname=" + lname +"&place=" + place + "&phone=" + phone + "&email=" + email + "&username="+ username + "&password=" + password+"&lati="+LocationService.lati+"&logi="+LocationService.logi ;
                q = q.replace(" ", "%20");
                JR.execute(q);

            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {
            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                Toast.makeText(getApplicationContext(), "REGISTRATION SUCCESS", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), login.class));

            } else if (status.equalsIgnoreCase("duplicate")) {
                startActivity(new Intent(getApplicationContext(), Sparepartsdeliveryboy.class));
                Toast.makeText(getApplicationContext(), "Username and Password already Exist...", Toast.LENGTH_LONG).show();

            }else if (status.equalsIgnoreCase("already")) {
                Toast.makeText(getApplicationContext(), "Username Or Password ALREADY EXIST", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), Sparepartsdeliveryboy.class));

            }else {
                startActivity(new Intent(getApplicationContext(), Sparepartsdeliveryboy.class));

                Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
}