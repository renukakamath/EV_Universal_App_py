package com.example.evuniversalapp;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
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

public class UserViewordereditems extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {
    ListView l1;
    SharedPreferences sh;
    String[] product_name,firstname,image,quantity,statu,total,value,user_id,sparepart_id,date,order_id,longitude,latitude;
    public static String sta,amt,oid,tlati,tlongi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_viewordereditems);
        l1=(ListView) findViewById(R.id.list);
        l1.setOnItemClickListener(this);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) UserViewordereditems.this;
        String q = "/UserViewordereditems?log_id=" +sh.getString("log_id", "");
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
                product_name = new String[ja1.length()];
                firstname = new String[ja1.length()];
                image = new String[ja1.length()];
                quantity = new String[ja1.length()];
                total = new String[ja1.length()];
                user_id = new String[ja1.length()];
                sparepart_id = new String[ja1.length()];
                date = new String[ja1.length()];
                statu = new String[ja1.length()];
                value = new String[ja1.length()];
                order_id = new String[ja1.length()];
                longitude = new String[ja1.length()];
                latitude = new String[ja1.length()];



                String[] value = new String[ja1.length()];

                for (int i = 0; i < ja1.length(); i++) {
                    product_name[i] = ja1.getJSONObject(i).getString("product_name");

                    firstname[i] = ja1.getJSONObject(i).getString("firstname");
                    image[i] = ja1.getJSONObject(i).getString("image");
                    quantity[i] = ja1.getJSONObject(i).getString("quantity");

                    total[i] = ja1.getJSONObject(i).getString("total");
                    user_id[i] = ja1.getJSONObject(i).getString("user_id");
                    sparepart_id[i] = ja1.getJSONObject(i).getString("sparepart_id");


                    date[i] = ja1.getJSONObject(i).getString("date");

                    statu[i] = ja1.getJSONObject(i).getString("status");
                    order_id[i] = ja1.getJSONObject(i).getString("order_id");
                    longitude[i] = ja1.getJSONObject(i).getString("longitude");
                    latitude[i] = ja1.getJSONObject(i).getString("latitude");





                    value[i] = " Product Name:" + product_name[i] + "\nSpareparts Name: " + firstname[i] + "\n quantity: " + quantity[i] + "\nAmount: " + total[i]  + "\nstatus: " + statu[i]  + "\ndate: " + date[i] ;

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);
                Custimage1 a = new Custimage1(this, product_name, firstname,image,quantity,statu,total,date);
                l1.setAdapter(a);

            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();

        }
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        sta=statu[i];
        amt=total[i];
        oid=order_id[i];
        tlati=latitude[i];
        tlongi=longitude[i];


        if (sta.equalsIgnoreCase("pending")) {

            final CharSequence[] items = {"Pay Now" , "Cancel"};

            AlertDialog.Builder builder = new AlertDialog.Builder(UserViewordereditems.this);
            builder.setItems(items, new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int item) {


                    if (items[item].equals("Pay Now")) {

                        startActivity(new Intent(getApplicationContext(), Usermakepayments.class));


                    }  else if (items[item].equals("Cancel")) {
                        dialog.dismiss();
                    }
                }

            });
            builder.show();
        }else if (sta.equalsIgnoreCase("Paid")) {

            final CharSequence[] items = {"view Location","Rate","Cancel"};

            AlertDialog.Builder builder = new AlertDialog.Builder(UserViewordereditems.this);
            builder.setItems(items, new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int item) {

                    if (items[item].equals("view Location")) {


                        //                    startActivity(new Intent(getApplicationContext(),UserHotelRoomBooking.class));
                        String url = "http://www.google.com/maps?saddr=" + LocationService.lati + "" + "," + LocationService.logi + "" + "&&daddr=" + tlati + "," + tlongi;

                        Intent in = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                        startActivity(in);





                    } else if (items[item].equals("Rate")) {

                        startActivity(new Intent(getApplicationContext(), Rateings.class));

                    }else if (items[item].equals("Cancel")) {
                        dialog.dismiss();
                    }

                }

            });
            builder.show();
        }
    }
}