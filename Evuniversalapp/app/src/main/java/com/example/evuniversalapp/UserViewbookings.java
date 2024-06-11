package com.example.evuniversalapp;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class UserViewbookings extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {
    ListView l1;
    SharedPreferences sh;
    String[] vehicle,first_name,amount,date,statu,vehicle_id,value,request_id;
    public static String amt,rid;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_viewbookings);
        l1=(ListView) findViewById(R.id.list);
        l1.setOnItemClickListener(this);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) UserViewbookings.this;
        String q = "/UserViewbookings?log_id=" +sh.getString("log_id", "");
        q = q.replace(" ", "%20");
        JR.execute(q);
    }

    @Override
    public void response(JSONObject jo) {
        try {

            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");
                vehicle = new String[ja1.length()];
                first_name = new String[ja1.length()];
                amount = new String[ja1.length()];
                date = new String[ja1.length()];
                statu = new String[ja1.length()];
                request_id = new String[ja1.length()];


                value = new String[ja1.length()];



                String[] value = new String[ja1.length()];

                for (int i = 0; i < ja1.length(); i++) {
                    vehicle[i] = ja1.getJSONObject(i).getString("vehicle");

                    first_name[i] = ja1.getJSONObject(i).getString("first_name");
                    amount[i] = ja1.getJSONObject(i).getString("amount");
                    date[i] = ja1.getJSONObject(i).getString("date");
                    statu[i] = ja1.getJSONObject(i).getString("status");
                    request_id[i] = ja1.getJSONObject(i).getString("request_id");



                    value[i] = "vehicle:" + vehicle[i] + "\nfirst_name: " + first_name[i] + "\n amount: " + amount[i] + "\ndate: " + date[i] +"\nstatus:"+ statu[i]  ;

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);

            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();

        }
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        amt=amount[i];
        rid=request_id[i];
        final CharSequence[] items = {"Pay Now","Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder(UserViewbookings.this);
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {

                if (items[item].equals("Pay Now")) {


                    startActivity(new Intent(getApplicationContext(), UserMakePayment.class));



                }



                else if (items[item].equals("Cancel")) {


                    dialog.dismiss();
                }
            }

        });
        builder.show();
    }
}